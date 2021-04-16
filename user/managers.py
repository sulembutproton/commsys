from django.contrib.auth.models import BaseUserManager
from django.db import models
import logging

logger = logging.getLogger(__name__)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must emter an email address')
        if not password:
            raise ValueError('User must enter a password')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        logger.info('New user with Name: {} {} and email: {} has been created'.format(
            kwargs.get('first_name'), kwargs.get('last_name'), email
        ))
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('admin', False)
        kwargs.setdefault('staff', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('staff', True)
        kwargs.setdefault('admin', True)
        if kwargs.get('staff') is not True:
            raise ValueError('Superuser must have permission "staff" = True')
        if kwargs.get('admin') is not True:
            raise ValueError('Superuser must have permission "admin" = True')
        return self._create_user(email, password, **kwargs)
