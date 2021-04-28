from django.db.models import CharField, DecimalField, BooleanField, TextField, EmailField, ManyToManyField
from django.db.models import Model
#from .property import Property
from decimal import Decimal
from django.core.validators import MinValueValidator



GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class People(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    gender = CharField(max_length=50, choices=GENDER)
    email = EmailField(max_length=100)
    mobile_number = CharField(max_length=18)
    address = CharField(max_length=200)
    #interest = ManyToManyField("Property", through='Membership', related_name='+', blank=True)
    budget = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))], blank=True,
                          null=True)
    preference = CharField(max_length=100, blank=True, null=True)
    purpose = CharField(max_length=100, blank=True, null=True)
    looking = BooleanField(default=True)
    description = TextField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    def __str__(self):
        return "(%s(%s)) : %s %s" % (
            self.__class__.__name__,
            self.pk,
            self.first_name,
            self.last_name
        )
