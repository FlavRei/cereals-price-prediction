import os
from google.cloud import storage
from google.cloud.storage import Client, transfer_manager

def upload_files_to_gcs(bucket_name, source_directory="", workers=8):
    """Upload every file from a source_directory to a bucket.
    :param bucket_name: GCS bucket name
    :param source_directory: local path
    """

    storage_client = Client("cereals-price-prediction")
    bucket = storage_client.bucket(bucket_name)

    filenames = []
    for filename in os.listdir(source_directory):
        if filename.endswith(".csv"):
            filenames.append(filename)

    results = transfer_manager.upload_many_from_filenames(
        bucket, filenames, source_directory=source_directory, max_workers=workers
    )

    for name, result in zip(filenames, results):
        if isinstance(result, Exception):
            print("Failed to upload {} due to exception: {}".format(name, result))
        else:
            print("Uploaded {} to {}.".format(name, bucket.name))

if __name__ == "__main__":
    upload_files_to_gcs(
        bucket_name="cereals-data-bucket",
        source_directory="data"
    )
