from django import forms
from .models import Package, Location, Checkout, Shipment, Packaging, Contact
from django_countries.fields import CountryField
from django_countries import countries



class QuoteForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = [
            'pickup_country',
            'delivery_country',
            'weight',
            'length',
            'width',
            'height',
        ]
    
    pickup_country = CountryField().formfield()
    pickup_zip = forms.IntegerField()
    delivery_country = CountryField().formfield()
    delivery_zip = forms.IntegerField()
    weight = forms.IntegerField()
    length = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        exclude = ('package',)

    # Shipment fields
    create_shipment = forms.BooleanField(required=False)
    pay = forms.BooleanField(required=False)
    print = forms.BooleanField(required=False)

    # Senders information fields
    sender_name = forms.CharField(max_length=100)
    sender_company = forms.CharField(max_length=100, required=False)
    sender_pickup_country = forms.CharField(max_length=100, required=False)
    sender_address = forms.CharField(max_length=200)
    sender_address2 = forms.CharField(max_length=200, required=False)
    sender_address3 = forms.CharField(max_length=200, required=False)
    sender_pickup_zip = forms.CharField(max_length=100, required=False)
    sender_city = forms.CharField(max_length=100)
    sender_state = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    sender_phone_type = forms.CharField(max_length=100)
    sender_phone_code = forms.CharField(max_length=10)
    sender_phone_number = forms.CharField(max_length=20)

    # Receivers information fields
    receiver_name = forms.CharField(max_length=100)
    receiver_company = forms.CharField(max_length=100, required=False)
    receiver_delivery_country = forms.CharField(max_length=100, required=False)
    receiver_address = forms.CharField(max_length=200)
    receiver_address2 = forms.CharField(max_length=200, required=False)
    receiver_address3 = forms.CharField(max_length=200, required=False)
    receiver_delivery_zip = forms.CharField(max_length=100, required=False)
    receiver_city = forms.CharField(max_length=100)
    receiver_state = forms.CharField(max_length=100)
    receiver_email = forms.EmailField()
    receiver_phone_type = forms.CharField(max_length=100)
    receiver_phone_code = forms.CharField(max_length=10)
    receiver_phone_number = forms.CharField(max_length=20)
    vat_tax_id = forms.CharField(max_length=100, required=False)

    # Quote fields

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        

    def clean(self):
        cleaned_data = super().clean()
        package_id = self.request.session.get('package_id')
        if package_id is not None:
            package = Package.objects.get(package_id=package_id)
            cleaned_data['package'] = package

        return cleaned_data


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['shipping_type', 'description', 'value', 'item_description', 'manufacturer_id', 'quantity', 'units', 'item_value', 'schedule_b', 'reference', 'invoice_value']

    def clean(self):
        cleaned_data = super().clean()

        if 'documents' in self.data:
            cleaned_data['shipment_type'] = 'Documents'
        elif 'packages' in self.data:
            cleaned_data['shipment_type'] = 'Packages'

        return cleaned_data

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class EditShippingForm(forms.ModelForm):

    class Meta:
        model = Checkout
        fields = ['sender_name', 'sender_company', 'sender_pickup_country', 'sender_address', 'sender_address2', 'sender_address3', 'sender_pickup_zip', 'sender_city', 'sender_state', 'sender_email', 'sender_phone_type', 'sender_phone_code', 'sender_phone_number', 'receiver_name', 'receiver_company', 'receiver_delivery_country', 'receiver_address', 'receiver_address2', 'receiver_address3', 'receiver_delivery_zip', 'receiver_city', 'receiver_state','receiver_email', 'receiver_phone_type', 'receiver_phone_code','receiver_phone_number', 'vat_tax_id']
    
    sender_name = forms.CharField(required=False)
    sender_pickup_country = forms.CharField(required=False)
    sender_address = forms.CharField(required=False)
    sender_pickup_zip = forms.IntegerField(required=False)
    sender_city = forms.CharField(required=False)
    sender_state = forms.CharField(required=False)
    sender_email = forms.EmailField(required=False)
    sender_phone_type = forms.CharField(required=False)
    sender_phone_code = forms.CharField(required=False)
    sender_phone_number = forms.IntegerField(required=False)
    receiver_name = forms.CharField(required=False)
    receiver_address = forms.CharField(required=False)
    receiver_delivery_country = forms.CharField(required=False)
    receiver_delivery_zip = forms.IntegerField(required=False)
    receiver_state = forms.CharField(required=False)
    receiver_city = forms.CharField(required=False)
    receiver_email = forms.EmailField(required=False)
    receiver_phone_type = forms.CharField(required=False)
    receiver_phone_code = forms.CharField(required=False)
    receiver_phone_number = forms.IntegerField(required=False)


class EditShipmentForm(forms.ModelForm):

    class Meta:
        model = Shipment
        fields = ['status', 'shipping_type', 'description', 'value', 'item_description', 'manufacturer_id', 'quantity', 'units', 'item_value', 'schedule_b', 'reference', 'invoice_value']
    
            
class PackagingForm(forms.ModelForm):
    class Meta:
        model = Packaging
        fields = [
            'packaging_type',
            'quantity',
            'weight',
            'length',
            'width',
            'height',
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_country_code', 'phone_number', 'phone_type', 'address', 'address2', 'address3', 'city', 'state', 'zip_code', 'country']
        
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    phone_country_code = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    phone_type = forms.CharField(required=False)
    address = forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    address3 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    country = forms.CharField(required=False)

class PaymentForm(forms.Form):
    CARD_TYPE = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
    ]
    CARD_BRANDS = [
        ('visa', 'Visa'),
        ('mastercard', 'Mastercard'),
        ('discover', 'Discover'),
        ('amex', 'American Express'),
    ]
    card_type = forms.ChoiceField(choices=CARD_TYPE, required=True)
    card_brand = forms.ChoiceField(choices=CARD_BRANDS, required=True)
    cardholder_name = forms.CharField(required=True)
    card_number = forms.CharField(required=True)
    card_expiry_month = forms.IntegerField(required=True)
    card_expiry_year = forms.IntegerField(required=True)
    card_cvv = forms.IntegerField(required=True)


class ShipmentTrackingForm(forms.Form):
    package_id = forms.CharField(max_length=100, label='Track your shipment')

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['sender', 'pickup_country', 'delivery_country', 'weight']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address']

