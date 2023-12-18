from django.apps import AppConfig


class PhonebookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phonebook'

    # Flaw 5: Uncomment the two lines below to fix
    # def ready(self):
    #     from . import signals
