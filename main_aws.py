from database_aws import connect_to_database, create_instances_table, create_audit_table, \
    truncate_table, insert_instance_id, select_instance_ids
from ec2_instance_aws import EC2Instance
# print("hello")
def main():
    connect = connect_to_database()
    cursor = connect.cursor()

    create_instances_table(cursor)
    create_audit_table(cursor)

    truncate_table(cursor, 'instances')
    truncate_table(cursor, 'audit')

    ec2_instance = EC2Instance("key", "secret_access_key",cursor,connect)

    while True:
        instance_id = input("Enter the instance ID: ")
        if instance_id.lower() == 'done':
            break
        insert_instance_id(cursor, instance_id)
        connect.commit()

    instance_ids = select_instance_ids(cursor)

    for instance_id in instance_ids:
        ec2_instance.start_valid_instance(instance_id)
        # Fetch the next row
        # row = cursor.fetchone()  

    action = input("Enter '1' to stop the previously started instance: ")
    if action == '1':
        if ec2_instance.started_instance_id is not None:
            ec2_instance.stop_started_instances_by_start_function(ec2_instance.started_instance_id)
        else:
            print("No instance has been started.")
    else:
        print("Invalid input.")
        instance_id = input("Enter the instance ID to stop: ")
        ec2_instance.stop_started_instances_by_start_function(instance_id)

    cursor.close()
    connect.close()

if __name__ == "__main__":
    main()
