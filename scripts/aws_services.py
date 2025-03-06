import boto3
import extract_gdelt
import pandas as pd
import io
from dotenv import load_dotenv
import os

load_dotenv()
awsConfig = extract_gdelt.config["aws"]
AWS_S3_BUCKET = awsConfig["s3_bucket"]
AWS_ACCESS_KEY_ID = os.getenv("aws_access_key")
AWS_SECRET_ACCESS_KEY = os.getenv("aws_secrete")


s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def writeToS3(df, key):
    with io.StringIO() as csv_buffer:
        df.to_csv(csv_buffer, index=False)
        response = s3_client.put_object(
            Bucket=AWS_S3_BUCKET, Key=key, Body=csv_buffer.getvalue()
        )
