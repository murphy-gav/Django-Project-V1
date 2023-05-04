from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from .models import Checkout, Package, LocationDistance, Shipment, Packaging, Contact, Payment, Location, Stations
from django.contrib.auth.decorators import user_passes_test

# Register your models here.
admin.site.register(Checkout)
admin.site.register(Packaging)
admin.site.register(Location)
admin.site.register(Stations)
admin.site.register(Shipment)
admin.site.register(Package)
admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(LocationDistance)




class Admin(User):
    is_admin = models.BooleanField(default=False)


def is_admin(user):
    return user.is_authenticated and user.is_admin

@user_passes_test(is_admin)
def report_view(request):
    # generate report
    ...
