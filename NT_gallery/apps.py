from django.apps import AppConfig


class NtGalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NT_gallery'

    def ready(self):
        import NT_gallery.signals  # Import the signals here
