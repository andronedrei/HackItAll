from django.apps import AppConfig


class HackAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        print("API app is ready")
        try:
            import api.signals
            print("SIGNALS IMPORTED SUCCESSFULLY")
        except ImportError:
            print(f"ERROR IMPORTING SIGNALS: {ImportError}")
