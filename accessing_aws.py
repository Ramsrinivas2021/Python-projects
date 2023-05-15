import boto3

# Set up the AWS credentials
aws_access_key_id = 'aws_access_key_id'
aws_secret_access_key = 'aws_secret_access_key'

# Set up the EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,region_name='us-east-1')

# Specify the instance ID of the EC2 instance you want to start or stop
instance_id = input("Enter instance_id to start or stop the EC2 instance: ")

# Start the EC2 instance
ec2.start_instances(InstanceIds=[instance_id])
print(f"Started instance {instance_id}")

# Stop the EC2 instance
ec2.stop_instances(InstanceIds=[instance_id])
print(f"Stopped instance {instance_id}")

