from re import S
from google.cloud import storage
from google.cloud.storage import bucket


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    # uploads file to bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(source_file_name)

    print("File {} uploaded as {}.".format(source_file_name, destination_blob_name))


def get_profile_pic(bucket_name, filename):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    return blob.public_url

def file_in_storage(bucket_name, filename):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    return blob.exists()