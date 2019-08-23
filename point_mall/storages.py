import boto3
from storages.backends.s3boto3 import S3Boto3Storage


from . import settings

class FileStorage(S3Boto3Storage):
    pass


class StaticStorage(FileStorage):
    location = settings.STATIC_ROOT