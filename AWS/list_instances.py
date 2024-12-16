import boto3

def list_instances():
    ec2 = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

    for region in regions:
        print(f"Region: {region}")
        ec2 = boto3.client('ec2', region_name=region)
        instances = ec2.describe_instances()
        
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                instance_type = instance['InstanceType']
                public_ip = instance.get('PublicIpAddress', 'N/A')
                print(f"  Instance ID: {instance_id}")
                print(f"  State: {instance_state}")
                print(f"  Type: {instance_type}")
                print(f"  Public IP: {public_ip}")
                print("-" * 20)

if __name__ == "__main__":
    list_instances()
