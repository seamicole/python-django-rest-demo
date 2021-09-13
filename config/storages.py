# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from storages.backends.s3boto3 import S3Boto3Storage

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.conf import settings


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ STATIC STORAGE
# └─────────────────────────────────────────────────────────────────────────────────────


class StaticStorage(S3Boto3Storage):
    """ Amazon AWS S3 StaticStorage Class """

    # Enable file overwriting
    file_overwrite = True

    # Set default ACL
    default_acl = "public-read"

    # Define bucket name
    bucket_name = settings.AWS_STATIC_BUCKET_NAME

    # Define location in bucket
    location = settings.STATICFILES_LOCATION


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ MEDIA STORAGE
# └─────────────────────────────────────────────────────────────────────────────────────


class MediaStorage(S3Boto3Storage):
    """ Amazon AWS S3 MediaStorage Class """

    # Disable file overwriting
    file_overwrite = False

    # Set default ACL
    default_acl = None

    # Define bucket name
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # Define location in bucket
    location = settings.MEDIAFILES_LOCATION
