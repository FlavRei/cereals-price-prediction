import os
from google.cloud.storage import Client

def upload_files_to_gcs(bucket_name, source_directory, destination_directory):
    """Upload every file from a source_directory to a bucket.
    :param bucket_name: GCS bucket name
    :param source_directory: local path
    :param destination_directory: GCS path
    """

    storage_client = Client("cereals-price-prediction")
    bucket = storage_client.bucket(bucket_name)
    
    for filename in os.listdir(source_directory):
        if filename.endswith(".csv"):
            local_file = os.path.join(source_directory, filename)
            blob_name = f"{destination_directory}/{filename}"
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(local_file)
            print(f"File {filename} uploaded to gs://{bucket_name}/{blob_name}")

if __name__ == "__main__":
    upload_files_to_gcs(
        bucket_name="cereals-data-bucket",
        source_directory="data/raw",
        destination_directory="raw"        
    )
    upload_files_to_gcs(
        bucket_name="cereals-data-bucket",
        source_directory="data/clean",
        destination_directory="clean"
    )
