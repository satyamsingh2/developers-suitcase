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
