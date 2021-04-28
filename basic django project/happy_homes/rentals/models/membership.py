from django.db.models import CASCADE, ForeignKey,CharField, DecimalField, BooleanField, TextField, EmailField, ManyToManyField
from django.db.models import Model
from .people import People
from .owners import Owner


STATUS = (
    ('A', 'Active'),
    ('I', 'Inactive')
)
TYPE = (
    ('O', 'Owner'),
    ('P', 'PEOPLE')
)

class Membership(Model):
    name = CharField(max_length=100)
    owner = ForeignKey(Owner, on_delete=CASCADE, blank=True, null=True)
    people = ForeignKey(People, on_delete=CASCADE, blank=True, null=True)
    status = CharField(max_length=50, choices=STATUS)
    type = CharField(max_length=50, choices=TYPE)

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __str__(self):
        return "(%s(%s)) : %s" % (
            self.__class__.__name__,
            self.pk,
            self.name
        )