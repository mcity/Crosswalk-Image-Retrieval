import os
import requests
from dotenv import load_dotenv
import boto3

#Load environment variables from .env file.
load_dotenv()

#Short method to upload to S3
def upload_file(file, filename):
    """
    S3 Upload file
    """

    if file and filename:
        s3_bucket = boto3.resource('s3',
                                   aws_access_key_id=os.environ.get('S3_KEY', None),
                                   aws_secret_access_key=os.environ.get('S3_SECRET_ACCESS_KEY', None))
        bucket = s3_bucket.Bucket(os.environ.get('S3_BUCKET', None))
        bucket.upload_fileobj(file, filename)
        print ("Success", filename)
        return True
    else:
        print('No file found during upload or file is not of allowed types.')
        return False


#This is the URL to fetch, you could also give this as a command line 
#parameter with sys.argv[0] if you import sys.
fetch_url = os.environ.get('FETCH_URL', None)
if fetch_url:
    print ("fetching: ", fetch_url)
    response = requests.get(fetch_url, stream=True)
    if response.status_code == 200:
        upload_file(response.raw, "test_file.jpg")
    else:
        print ('Upload Failed.')
else:
    print ("No file specified.")