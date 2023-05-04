from django.contrib import admin
from django.urls import path

from globalwis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Swiftdrop App urls
    path('', views.HomeView.as_view(), name='home'),
    path('location/', views.LocationView.as_view(), name='location'),
    path('trackquote/', views.TrackQuoteView.as_view(), name='trackquote'),
    path('tracking/', views.TrackingView.as_view(), name='tracking'),
    path('success-history/', views.SuccessHistoryView.as_view(), name='successHistory'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('support/', views.SupportView.as_view(), name='support'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('quote/', views.QuotesCreateView.as_view(), {'action': 'create'}, name='quote'),
    path('create_shipment/', views.QuotesCreateView.as_view(), {'action': 'quote'}, name='create_shipment'),
    path('show-price/', views.show_price, name='show_price'),
    path('news/', views.news, name="news"),
    path('payment/<int:shipment_id>/', views.PaymentView.as_view(), name="payment"),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
    path('profile/', views.profile_view, name="profile"),
    path('manage_shipments/', views.ManageShipmentView.as_view(), name="manage_shipments"),
    path('track_shipment/', views.TrackShipmentView.as_view(), name='track_shipment'),
    path('user_information/', views.ContactDetailView.as_view(), name='user_information'),
    path('user_information_update/', views.ContactCreateUpdateView.as_view(), name='user_information_update'),
    path('create_edit/', views.ContactCreateUpdateView.as_view(), name='create_edit'),
    path('edit_shipment/', views.EditShipmentView.as_view(), name='edit_shipment'),
    path('edit_shipment_detials/', views.EditShipmentDetailsView.as_view(), name='edit_shipment_detials'),
    path('cancel_shipment/<str:package_id>/', views.cancel_shipment, name='cancel_shipment'),
    path('payment_success', views.payment_success, name='payment_success'), 
 

    # Shipment detials
    path('shipment-details/', views.ShipmentDetailsView.as_view(), name='shipment_details'),
    path('image_upload/<int:shipment_id>', views.ImageUploadView.as_view(), name='image_upload'),
    path('packaging/<int:shipment_id>/', views.PackagingView.as_view(), name='packaging'),
    path('shipment-confirmation/', views.ShipmentConfirmationView.as_view(), name='shipment_confirmation'),

    # Location URLs
    path('locations/', views.LocationListView.as_view(), name='location_list'),
    path('locations/create/', views.LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('locations/<int:pk>/update/', views.LocationUpdateView.as_view(), name='location_update'),
]
