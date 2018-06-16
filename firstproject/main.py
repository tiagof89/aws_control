import datetime
import boto3

AWS_DEFAULT_REGION = "eu-west-1"
dbinstance_name='out-autogest-bd-dev2'

def main():

    rds_conn = boto3.client('rds', region_name=AWS_DEFAULT_REGION)

    response = rds_conn.describe_db_instances(DBInstanceIdentifier=dbinstance_name)

    dbinstances = response['DBInstances']
    db_instance = dbinstances[0]
    status = db_instance['DBInstanceStatus']

    if (status == 'available'):
        status_output = rds_conn.stop_db_instance(
            DBInstanceIdentifier=dbinstance_name,
        )
        print(status_output)
    else:
        today = datetime.datetime.now()
        print(today, 'DB is',status)

if __name__ == '__main__':
    main()
