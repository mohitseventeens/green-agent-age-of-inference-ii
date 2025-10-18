import os
import argparse
from utils.s3_helper import S3Helper

def download_s3_prefix(bucket: str, prefix: str, local_dir: str):
    """
    Downloads all files from a specified S3 prefix to a local directory.

    Args:
        bucket (str): The name of the S3 bucket.
        prefix (str): The prefix (folder path) in the S3 bucket to download from.
        local_dir (str): The local directory to save the files to.
    """
    print("--- Starting S3 Data Download ---")
    
    s3_helper = S3Helper()
    
    print(f"Listing objects from bucket '{bucket}' with prefix '{prefix}'...")
    all_objects = s3_helper.list_objects(bucket)
    
    if not all_objects:
        print(f"❌ ERROR: No objects found in bucket '{bucket}'. Please check the bucket name and permissions.")
        return

    objects_to_download = [obj for obj in all_objects if obj['Key'].startswith(prefix)]
    
    if not objects_to_download:
        print(f"❌ ERROR: No objects found with the prefix '{prefix}'.")
        return

    print(f"Found {len(objects_to_download)} objects to download.")

    success_count, fail_count = 0, 0
    for i, obj in enumerate(objects_to_download):
        s3_key = obj['Key']
        
        # Skip directories themselves
        if s3_key.endswith('/'):
            continue

        local_path = os.path.join(local_dir, s3_key)
        
        print(f"Downloading [{i+1}/{len(objects_to_download)}]: {s3_key} -> {local_path}")
        
        if s3_helper.download_object(bucket, s3_key, local_path):
            success_count += 1
        else:
            fail_count += 1

    print("\n--- Download Summary ---")
    print(f"✅ Successfully downloaded: {success_count} files.")
    if fail_count > 0:
        print(f"❌ Failed to download: {fail_count} files. Check logs for errors.")
    
    print("\nDownload process complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A generic utility to download files from an S3 prefix to a local directory.")
    
    parser.add_argument("--bucket", required=True, help="The S3 bucket name.")
    parser.add_argument("--prefix", required=True, help="The S3 prefix (folder) to download from.")
    parser.add_argument("--local-dir", default=".", help="The local destination directory. Defaults to the current directory.")
    
    args = parser.parse_args()
    
    download_s3_prefix(args.bucket, args.prefix, args.local_dir)