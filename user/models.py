from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser):
    email           = models.EmailField(verbose_name=r'Email Address', unique=True)
    first_name      = models.CharField(max_length=60)
    last_name       = models.CharField(max_length=60)
    admin           = models.BooleanField(default=False)
    staff           = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return " ".join([self.first_name, self.last_name])

    def get_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_email(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin


class UserRole(models.Model):
    CUSTOMER = 10
    VENDOR = 20
    ROLES = (
        (CUSTOMER, 'Customer'), (VENDOR, 'Vendor')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='role')
    role = models.PositiveIntegerField(choices=ROLES, default=CUSTOMER)

    def get_role(self):
        return self.role

    def get_user(self):
        return self.user
