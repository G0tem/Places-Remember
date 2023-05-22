from django.apps import AppConfig


class VisitedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visited'

    # def ready(self):
    #     import visited.signals