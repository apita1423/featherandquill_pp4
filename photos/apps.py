from django.apps import AppConfig


class PhotosConfig(AppConfig):
    """
    Provides primary key type for birdblog
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photos'
