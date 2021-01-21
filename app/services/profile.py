from app.models import s3
from config.db import RemoteDBConfig


def upload_image_to_s3(image, image_name):
    s3.upload_fileobj(image, RemoteDBConfig.S3_BUCKET_NAME, image_name)