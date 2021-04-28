from django.db.models import CASCADE, CharField, ForeignKey, DecimalField, BooleanField, TextField
from django.db.models import Model
from .owners import Owner
from .people import People
from decimal import Decimal
from django.core.validators import MinValueValidator

STATUS = (
    ('sold', 'SOLD'),
    ('unsold', 'UNSOLD'),
)


class Property(Model):
    name = CharField(max_length=100)
    owner = ForeignKey(Owner, on_delete=CASCADE)
    price = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    type = CharField(max_length=100, blank=True, null=True)
    status = CharField(max_length=20, choices=STATUS)
    available = BooleanField(default=True)
    description = TextField(max_length=300, blank=True, null=True)
    people = ForeignKey(People, on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return "(%s(%s)) : %s : %s : (%s)" % (
            self.__class__.__name__,
            self.pk,
            self.name,
            self.owner,
            self.status
        )
