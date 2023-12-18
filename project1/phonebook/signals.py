# Flaw 5 fix

import logging
from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.dispatch import receiver
import datetime

logger = logging.getLogger('django')

def time():
    return datetime.datetime.now().strftime('%d/%b/%Y %H:%M:%S')

@receiver(user_logged_in)
def login(sender, request, user, **kwargs):
    logger.info(f'[{time()}]User: {user.username} logged in')

@receiver(user_logged_out)
def logout(sender, request, user, **kwargs):
    logger.info(f'[{time()} ]User: {user.username} logged out')

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    logger.warning(f'[{time()}] User: {credentials} failed to log in')