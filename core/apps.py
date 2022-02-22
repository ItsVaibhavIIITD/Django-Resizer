from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from core.scheduler import resize_images
        print("Application and Scheduler started!")
        resize_images.start()