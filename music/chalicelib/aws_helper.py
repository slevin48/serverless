import boto3
import botocore.exceptions


class S3:
    def __init__(self, bucket_name):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name
        if not self.check_if_bucket_exists():
            print("okay, bucket does not exist")
            self.create_bucket()
        else:
            print("bucket exists")

    def check_if_bucket_exists(self):
        try:
            self.s3.head_bucket(Bucket=self.bucket_name)
            return True
        except botocore.exceptions.ClientError:
            return False

    def create_bucket(self):
        print("Creating bucket: " + self.bucket_name)
        self.s3.create_bucket(Bucket=self.bucket_name)

    def upload_file(self, file_path, s3_path):
        self.s3.upload_file(file_path, self.bucket_name, s3_path)

    def download_file(self,s3_path):
        return self.s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": self.bucket_name,
                "Key": s3_path,
            },
            ExpiresIn=3600,
        )