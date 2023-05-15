import boto3
import mysql.connector
from datetime import datetime
from botocore.exceptions import ClientError


# Connect to the database
connect = mysql.connector.connect(
    host='localhost',
    port ='3306',
    user="srinivas.account",
    password='@123',
    database='instancesdb'
)


cursor = connect.cursor()
# Define the table creation query with auto-increment primary key
create_table_query = """
CREATE TABLE IF NOT EXISTS instances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    instance_id VARCHAR(255)
)
"""
cursor.execute(create_table_query)
connect.commit()
# Prepare the insert query
insert_query = "INSERT INTO instances (instance_id) VALUES (%s)"

    # Create the audit table if it doesn't exist
create_table_query2 = """
CREATE TABLE IF NOT EXISTS audit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    instance_id VARCHAR(20),
    start_time DATETIME,
    stop_time DATETIME,
    instance_state VARCHAR(20)
)
"""



cursor.execute(create_table_query2)
connect.commit()

# Defining a class for EC2 instances
class EC2Instance:
         # Constructor function to initialize the object
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        # Storing the AWS access keys as instance variables
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        # Creating an EC2 client using the access keys and the desired region
        self.ec2 = boto3.client('ec2', 
                                aws_access_key_id=self.aws_access_key_id, 
                                aws_secret_access_key=self.aws_secret_access_key, 
                                region_name='us-east-1')
        self.started_instance_id = None

    #EC2Instance class start function
    def start(self, instance_id):
         
        try:
            # Check if the instance ID is valid
            response = self.ec2.describe_instances(InstanceIds=[instance_id])
            if len(response['Reservations']) == 0:
                print(f"Invalid instance ID: {instance_id}")
                return
            instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidInstanceID.Malformed':
                print(f"Invalid instance ID: {instance_id}")
            else:
                print(f"An error occurred: {e}")
            return
        # Starting the EC2 instance using the instance ID
        self.ec2.start_instances(InstanceIds=[instance_id])
        # Printing a message to indicate that the instance is being started
        print(f"Starting instance {instance_id}...")
        # Waiting for the instance to be in the running state
        waiter = self.ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id],WaiterConfig={'MaxAttempts': 6, 'Delay': 10})
        # Get the instance state after it is running
        response = self.ec2.describe_instances(InstanceIds=[instance_id])
        instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
        # Get the current timestamp
        start_time = datetime.now()
        insert_query = "INSERT INTO audit (instance_id, start_time, stop_time, instance_state) VALUES (%s, %s, NULL, %s)"
        cursor.execute(insert_query, (instance_id, start_time, instance_state))
        connect.commit()
        # Printing a message to indicate that the instance has been started
        print(f"Instance {instance_id} has been started.")
        self.started_instance_id = instance_id

    # EC2Instance class stop function
    def stop(self, instance_id):
        self.ec2.stop_instances(InstanceIds=[instance_id])
        # Printing a message to indicate that the instance is being stopped
        print(f"Stopping instance {instance_id}...")
        # Waiting for the instance to be in the stopped state
        waiter = self.ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id],WaiterConfig={'MaxAttempts': 5, 'Delay': 10})
        # To Get the current timestamp
        stop_time = datetime.now()
        # print(stop_time)
        # Printing a message to indicate that the instance has been stopped
        print(f"Instance {instance_id} has been stopped.")
        update_query = "UPDATE audit SET stop_time = %s, instance_state = 'STOPPED' WHERE instance_id = %s AND stop_time IS NULL"
        cursor.execute(update_query, (stop_time, instance_id))
        connect.commit()  # Commit the changes to the database
        # Update the audit table with the stop time and state of the instance
        self.started_instance_id = None  # Reset the started instance ID
        

# # Creating an instance of the EC2Instance class with passing the AWS access keys as argument values
ec2_instance = EC2Instance("key",'secret_access_key')

# Truncate the instances table
truncate_instances_query = "TRUNCATE TABLE instances"
cursor.execute(truncate_instances_query)
connect.commit()

# Truncate the audit table
truncate_audit_query = "TRUNCATE TABLE audit"
cursor.execute(truncate_audit_query)
connect.commit()


# user  need to enter the instance ID which needs to be start and stop
while True:
    instance_id = input("Enter the instance ID: ")
    # Break  the loop if the user enters "done"
    if instance_id.lower() == 'done':
        break

    # Inserting the instance ID into the database
    cursor.execute(insert_query, (instance_id,))
    connect.commit()

cursor.close()
connect.close()

# Connect to the database again to retrieve instance IDs
connect = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='srinivas.account',
    password='@123',
    database='instancesdb'
)
cursor = connect.cursor()
select_query = "SELECT instance_id FROM instances"
# Execute the query to retrieve instance IDs
cursor.execute(select_query)
# Fetch one row at a time from the result set
rows = cursor.fetchall()
# Process each instance ID
for row in rows:
    instance_id = row[0]
    # Check if the instance ID is valid and start the instance if it is
    response = ec2_instance.start(instance_id)
    
    # Fetch the next row
    row = cursor.fetchone()  
# Ask user to stop the started instance
action = input("Enter '1' to stop the previously started instance: ")
if action == '1':
    if ec2_instance.started_instance_id is not None:
        ec2_instance.stop(ec2_instance.started_instance_id)
    else:
        print("No instance has been started.")
else:
    print("Invalid input.")
    ec2_instance.stop(instance_id)  
    # Ask for the instance ID again
    instance_id = input("Enter the instance ID to stop: ")
    ec2_instance.stop(instance_id)

cursor.close()
connect.close()
