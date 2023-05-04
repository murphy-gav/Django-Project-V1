from django.db import models
import requests
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_countries.fields import CountryField
from django.utils import timezone




# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code =  models.IntegerField(default=False)
    country =  models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, default=False)
    image = models.ImageField(default=False)

    def __str__(self):
        return self.name

    # add other fields as needed

class LocationDistance(models.Model):
    pickup_country = models.CharField(max_length=100)
    delivery_country = models.CharField(max_length=100)
    distance_km = models.FloatField()


class Package(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_country = models.CharField(max_length=255, default=False)
    delivery_country = models.CharField(max_length=255, default=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=False)
    width = models.DecimalField(max_digits=5, decimal_places=2, default=False)
    length = models.DecimalField(max_digits=5, decimal_places=2, default=False)
    package_id = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.package_id

class Checkout(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    sender_name = models.CharField(max_length=100, null=True)
    sender_company = models.CharField(max_length=100, blank=True, default=False)
    sender_pickup_country = models.CharField(max_length=200, blank=True, default=False, null=True)
    sender_address = models.CharField(max_length=200)
    sender_address2 = models.CharField(max_length=200, blank=True, default=False)
    sender_address3 = models.CharField(max_length=200, blank=True, default=False)
    sender_pickup_zip = models.IntegerField(blank=True, null=True)
    sender_city = models.CharField(max_length=100, null=True)
    sender_state = models.CharField(max_length=100, null=True)
    sender_email = models.EmailField()
    sender_phone_type = models.CharField(max_length=100, null=True)
    sender_phone_code = models.CharField(max_length=10, null=True)
    sender_phone_number = models.CharField(max_length=20, null=True)
    receiver_name = models.CharField(max_length=100, null=True)
    receiver_company = models.CharField(max_length=100, blank=True, default=False)
    receiver_delivery_country = models.CharField(max_length=200, blank=True, default=False, null=True)
    receiver_address = models.CharField(max_length=200)
    receiver_address2 = models.CharField(max_length=200, blank=True, default=False)
    receiver_address3 = models.CharField(max_length=200, blank=True, default=False)
    receiver_delivery_zip = models.IntegerField(blank=True, null=True)
    receiver_city = models.CharField(max_length=100, null=True)
    receiver_state = models.CharField(max_length=100, null=True)
    receiver_email = models.EmailField()
    receiver_phone_type = models.CharField(max_length=100, null=True)
    receiver_phone_code = models.CharField(max_length=10, null=True)
    receiver_phone_number = models.CharField(max_length=20, null=True)
    vat_tax_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.sender_name} to {self.receiver_name}"
    
class Packaging(models.Model):
    packaging_type = models.CharField(max_length=500, default=False)
    quantity = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.packaging_type

class Payment(models.Model):
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    card_type = models.CharField(max_length=20)
    card_brand = models.CharField(max_length=20)
    card_expiry_month = models.IntegerField()
    card_expiry_year = models.IntegerField()
    card_cvv = models.IntegerField()

    def __str__(self):
        return f"{self.cardholder_name}'s Card Details"

class Stations(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code =  models.IntegerField(default=False)
    country =  models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, default=False)
    agent_name = models.CharField(max_length=255)
    agent_contact = models.CharField(max_length=255)
    open_time = models.DateTimeField(default=timezone.now)
    close_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=5))

    def __str__(self):
        return self.name
    

class Shipment(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    image = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=255)
    origin = models.CharField(max_length=255, default=False, null=True)
    destination = models.CharField(max_length=255, default=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    shipping_type = models.CharField(max_length=10, choices=[('documents', 'Documents'), ('packages', 'Packages')], blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.ForeignKey(Checkout, on_delete=models.CASCADE, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item_description = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    units = models.CharField(max_length=10, blank=True, null=True)
    item_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    country_of_origin = models.CharField(max_length=255, blank=True, null=True)
    schedule_b = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    invoice_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    drop_off_location = models.ForeignKey(Stations, on_delete=models.CASCADE, null=True, blank=True, related_name='drop_off_shipments')
    pick_up_location = models.ForeignKey(Stations, on_delete=models.CASCADE, null=True, blank=True, related_name='pick_up_shipments')
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    current_state = models.CharField(max_length=255, blank=True, null=True)
    current_country = models.CharField(max_length=255, blank=True, null=True)
    current_zip = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.package.sender}'s Shipment"


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, default=False)
    country = models.CharField(max_length=200, blank=True, default=False)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True, default=False)
    address3 = models.CharField(max_length=200, blank=True, default=False)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone_type = models.CharField(max_length=100)
    phone_country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user}'s Contact Information"


class PackageCountByLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    count = models.IntegerField()

class PackageCountByLocationView(LoginRequiredMixin, ListView):
    model = PackageCountByLocation
    template_name = 'package_count_by_location.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(count=Count('pickup_location'))
        return qs


