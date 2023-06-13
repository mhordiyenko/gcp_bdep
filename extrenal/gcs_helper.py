"""Helper functions to work with GCS (Google Cloud Storage)"""

from google.cloud import storage


def upload_files_to_gcs(project_id, bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to GCS 

    Args:
        project_id (str): GCP Project ID to create Google Cloud Storage Client
        bucket_name (str): GCS bucket name
        source_file_name (str): Path+Name of the file to be uploaded to GCS
        destination_blob_name (str): Path+Name of the file where to store the source file in GCS
    """

    try:
        client = storage.Client(project=project_id)
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)
        print(f'The file {source_file_name} is uploaded to {destination_blob_name}')

    except:
        raise "Failed to upload file to GCS bucket."


def delete_gcs_directory(project_id, bucket_name, directory_name):
    """Deletes all file from GCS bucket directory

    Args:
        project_id (str): GCP Project ID to create Google Cloud Storage Client
        bucket_name (str): Google Cloud Storage bucket name which contains directory to delete
        directory_name (str): Google Cloud Storage directory name to delete (e.g. 'data/temp')
    """

    MAX_BATCH_SIZE = 1000

    storage_client = storage.Client(project=project_id)
    bucket = storage_client.get_bucket(bucket_or_name=bucket_name)

    def add_slash_to_path_if_needed(src_path):
        return src_path+'/' if src_path[-1] != '/' else src_path

    directory_name = add_slash_to_path_if_needed(directory_name)
    batch_number = 1
    while True:
        blobs = [blob for blob in bucket.list_blobs(max_results=MAX_BATCH_SIZE, prefix=directory_name)]
        if len(blobs)>0:
            print(f'batch number: {batch_number}')
            with storage_client.batch():
                for blob in blobs:
                    blob.delete()
                    print(f'Deleted object: {blob}')
                batch_number += 1
        else:
            break
