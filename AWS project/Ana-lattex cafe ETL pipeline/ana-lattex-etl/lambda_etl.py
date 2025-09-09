import boto3
import csv
import io

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        obj = s3.get_object(Bucket=bucket, Key=key)
        raw_data = obj["Body"].read().decode("utf-8").splitlines()

        reader = csv.reader(raw_data)
        cleaned_rows = []
        for row in reader:
            if row and len(row) >= 4:
                cleaned_rows.append(row)

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerows(cleaned_rows)
        s3.put_object(
            Bucket="ana-curated-dev",
            Key=key,
            Body=output.getvalue()
        )
    return {"status": "done"}
