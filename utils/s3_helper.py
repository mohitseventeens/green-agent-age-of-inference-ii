import boto3
import logging
from botocore.exceptions import ClientError
from typing import List, Dict, Any, Optional
import os
import shutil # <-- IMPORT SHUTIL for robust cleanup

# --- FIX: Moved logger configuration to the top level ---
# Configure logging for the module
logger = logging.getLogger(__name__)
# Ensure logger has handlers (important for notebooks or standalone scripts)
if not logger.handlers:
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
# ---------------------------------------------------------

class S3Helper:
    """
    A helper class for common Amazon S3 operations.

    Provides methods to list, upload, and download objects from S3 buckets,
    with improved error handling, logging, and flexibility.
    """

    def __init__(self, region_name: Optional[str] = None):
        """
        Initializes the S3Helper with a Boto3 S3 client.

        Args:
            region_name (Optional[str]): The AWS region to use for the S3 client.
                                         If None, Boto3's default region resolution
                                         (e.g., from environment variables, config files)
                                         will be used.
        """
        if region_name:
            self.s3_client = boto3.client('s3', region_name=region_name)
            logger.info(f"S3Helper initialized for region: {region_name}")
        else:
            self.s3_client = boto3.client('s3')
            logger.info("S3Helper initialized using default region resolution.")

    def list_objects(self, bucket_name: str) -> List[Dict[str, Any]]:
        """
        Lists objects within a specified S3 bucket.

        Args:
            bucket_name (str): The name of the S3 bucket.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, where each dictionary
                                  contains 'Key' (object key) and 'LastModified'
                                  (creation/last modified time) for each object.
                                  Returns an empty list if no objects are found
                                  or an error occurs.
        """
        objects_info = []
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name)

            if 'Contents' in response:
                for obj in response['Contents']:
                    objects_info.append({
                        'Key': obj['Key'],
                        'LastModified': obj['LastModified']
                    })
                logger.info(f"Found {len(objects_info)} objects in bucket: {bucket_name}")
            else:
                logger.info(f"No objects found in bucket: {bucket_name}")
    
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucket':
                logger.error(f"Bucket '{bucket_name}' does not exist.")
            else:
                logger.error(f"Client error listing objects in '{bucket_name}': {e}")
        except Exception as e:
            logger.error(f"Unexpected error listing objects in '{bucket_name}': {e}", exc_info=True)
            
        return objects_info

    def upload_file(self, local_file_path: str, bucket_name: str, s3_object_key: str) -> bool:
        """
        Uploads a file from a local path to an S3 bucket.

        Args:
            local_file_path (str): The local path to the file to upload.
            bucket_name (str): The name of the target S3 bucket.
            s3_object_key (str): The desired key (path) for the object in S3.

        Returns:
            bool: True if the file was uploaded successfully, False otherwise.
        """
        if not os.path.exists(local_file_path):
            logger.error(f"Local file '{local_file_path}' not found.")
            return False

        try:
            self.s3_client.upload_file(local_file_path, bucket_name, s3_object_key)
            logger.info(f"File '{local_file_path}' uploaded to '{bucket_name}/{s3_object_key}'")
            return True
        except ClientError as e:
            logger.error(f"Client error uploading '{local_file_path}' to '{bucket_name}/{s3_object_key}': {e}")
        except Exception as e:
            logger.error(f"Unexpected error uploading '{local_file_path}' to '{bucket_name}/{s3_object_key}': {e}", exc_info=True)
        return False
            
    def download_object(self, bucket_name: str, s3_object_key: str, local_file_path: str) -> bool:
        """
        Downloads an object from an S3 bucket to a local file path.

        Args:
            bucket_name (str): The name of the S3 bucket.
            s3_object_key (str): The key (path) of the object in S3.
            local_file_path (str): The desired local path to save the downloaded file.

        Returns:
            bool: True if the object was downloaded successfully, False otherwise.
        """
        try:
            # Ensure the directory for local_file_path exists
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            
            self.s3_client.download_file(bucket_name, s3_object_key, local_file_path)
            logger.info(f"Object '{s3_object_key}' downloaded from '{bucket_name}' to '{local_file_path}'")
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                logger.error(f"Object '{s3_object_key}' not found in bucket '{bucket_name}'.")
            else:
                logger.error(f"Client error downloading '{s3_object_key}' from '{bucket_name}': {e}")
        except Exception as e:
            logger.error(f"Unexpected error downloading '{s3_object_key}' from '{bucket_name}': {e}", exc_info=True)
        return False

# --- NEW: Self-testing and usage example block ---
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # This is an example bucket. Replace with a real one for testing.
    # NOTE: Ensure your SageMaker execution role has permissions for this bucket.
    TEST_BUCKET = "age-of-inference-ii-dataset" 
    
    print(f"--- Running S3Helper Self-Test against bucket: {TEST_BUCKET} ---")
    
    helper = S3Helper()
    
    print("\n1. Testing: list_objects()")
    objects = helper.list_objects(TEST_BUCKET)
    if objects:
        print(f"✅ SUCCESS: Found {len(objects)} objects. Sample object key: '{objects[0]['Key']}'")
    else:
        print("⚠️ WARNING: Test finished, but no objects were found or an error occurred.")
    
    print("\n2. Testing: download_object() (Example)")
    if objects:
        sample_key = next((obj['Key'] for obj in objects if not obj['Key'].endswith('/')), None)
        
        if sample_key:
            temp_dir = "temp_s3_test"
            local_path = os.path.join(temp_dir, sample_key)
            
            print(f"Attempting to download '{sample_key}' to '{local_path}'...")
    
            success = helper.download_object(TEST_BUCKET, sample_key, local_path)
            if success and os.path.exists(local_path):
                print(f"✅ SUCCESS: File downloaded successfully.")
                # --- FIX: Use shutil.rmtree for robust cleanup ---
                print(f"Cleaning up temporary directory: {temp_dir}")
                shutil.rmtree(temp_dir)
                # --------------------------------------------------
            else:
                print("❌ FAILED: Download test failed. Check logs.")
        else:
            print("Skipping download test as no file objects were found (only directories).")
    
    print("\n--- Self-Test Complete ---")