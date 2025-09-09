import boto3
import csv
import psycopg2
import os

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = obj['Body'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(data)

    # Connect to Redshift
    conn = psycopg2.connect(
        dbname=os.environ['REDSHIFT_DB'],
        user=os.environ['REDSHIFT_USER'],
        password=os.environ['REDSHIFT_PASSWORD'],
        host=os.environ['REDSHIFT_HOST'],
        port=os.environ['REDSHIFT_PORT']
    )
    cur = conn.cursor()

    for row in reader:
        # Example: insert branch
        cur.execute(
            "INSERT INTO branches (branch_name) VALUES (%s) ON CONFLICT DO NOTHING",
            (row['branch_name'],)
        )
    conn.commit()
    cur.close()
    conn.close()
    return {"statusCode": 200, "body": f"{key} processed successfully"}
