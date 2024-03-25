from django.apps import AppConfig


class BirdblogConfig(AppConfig):
    """
    Provides primary key type for birdblog
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'birdblog'
