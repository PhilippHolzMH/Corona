from createjson import catch_cases
from creates3 import create_bucket
import boto3
from creates3 import s3_client
s3_client = boto3.client('s3', 'eu-central-1')

catch_cases("austria")  
create_bucket("bucket-fmv-445", "eu-central-1",s3_client)
s3_client.upload_file("rawdata.json", "bucket-fmv-445","rawdata.json")

