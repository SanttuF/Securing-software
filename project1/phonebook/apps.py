from django.apps import AppConfig


class PhonebookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phonebook'

    # Flaw 5: To fix uncomment the two lines below
    # def ready(self):
    #     from . import signals
