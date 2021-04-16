from django.db import models
from user.models import User


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    name = models.CharField(max_length=50)
    contact_numbers = models.CharField(max_length=12)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=12)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return ", ".join([
            self.name,
            self.contact_numbers,
            self.address1,
            self.address2,
            self.city,
            self.zipcode,
            self.state,
            self.country,
        ])
