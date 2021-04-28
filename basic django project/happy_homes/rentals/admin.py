from django.contrib import admin
from .models.owners import Owner
from .models.property import Property
from .models.people import People
from .models.membership import Membership

# Register your models here.
admin.site.register(Owner)
admin.site.register(Property)
admin.site.register(People)
admin.site.register(Membership)