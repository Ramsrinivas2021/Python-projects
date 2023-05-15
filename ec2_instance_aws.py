import boto3    
from datetime import datetime
from botocore.exceptions import ClientError

class EC2Instance:
    def __init__(self, aws_access_key_id, aws_secret_access_key,cursor,connect):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.ec2 = boto3.client('ec2', 
                                aws_access_key_id=self.aws_access_key_id, 
                                aws_secret_access_key=self.aws_secret_access_key, 
                                region_name='us-east-1')
        self.started_instance_id = None
        self.cursor = cursor
        self.connect = connect

    def validate_instance_id(self, instance_id):
        
        try:
            response = self.ec2.describe_instances(InstanceIds=[instance_id])
            if len(response['Reservations']) == 0:
                print(f"Invalid instance ID: {instance_id}")
                return False
            self.instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidInstanceID.Malformed':
                print(f"Invalid instance ID: {instance_id}")
            else:
                print(f"An error occurred: {e}")
            return False
        return True
        

    def start_valid_instance(self, instance_id):
        if not self.validate_instance_id(instance_id):
            return 

        self.ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}...")
        waiter = self.ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id], WaiterConfig={'MaxAttempts': 6, 'Delay': 10})
        response = self.ec2.describe_instances(InstanceIds=[instance_id])
        self.instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']
        start_time = datetime.now()
        insert_query = "INSERT INTO audit (instance_id, start_time, stop_time, instance_state) VALUES (%s, %s, NULL, %s)"
        self.cursor.execute(insert_query, (instance_id, start_time, self.instance_state))
        self.connect.commit()
        print(f"Instance {instance_id} has been started.")
        self.started_instance_id = instance_id

    def stop_started_instances_by_start_function(self, instance_id):
        self.ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id}...")
        waiter = self.ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id], WaiterConfig={'MaxAttempts': 5, 'Delay': 10})
        stop_time = datetime.now()
        print(f"Instance {instance_id} has been stopped.")
        update_query = "UPDATE audit SET stop_time = %s, instance_state = 'STOPPED' WHERE instance_id = %s AND stop_time IS NULL"
        self.cursor.execute(update_query, (stop_time, instance_id))
        self.connect.commit()

        self.started_instance_id = None 
