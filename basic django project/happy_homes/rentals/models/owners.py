from django.db.models import CharField, EmailField, TextField
from django.db.models import Model

class Owner(Model):
    name = CharField(max_length=100)
    email = EmailField(max_length=100)
    mobile_number = CharField(max_length=18)
    address = CharField(max_length=200)
    description = TextField(max_length=300, blank=True)

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

    def __str__(self):
        return "(%s(%s)) : %s" % (
            self.__class__.__name__,
            self.pk,
            self.name
        )

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

"""
the below one is for generating token with the help of signal 
in this as we create user token is automatically generated 
"""

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

"""
if you already have some user and u want to create token for all existing user
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
    Token.objects.get_or_create(user=user)
    
"""

