from django.urls import path
from . import views
from ui.views import CreateCheckoutSessionView

app_name = "ui"



urlpatterns = [
    path('',views.home,name="home"),
    path('tours',views.tours,name="tours"),
    path('stripe/webhooks',views.stripe_webhook,name="stripe_webhook"),
    path('success/',views.success,name="success"),
    path('cancel/',views.canceled,name="cancel"),
    path('create-checkout-session/<slug:slug>',views.CreateCheckoutSessionView,name="create-checkout-session"),
    path('tour/<slug:slug>',views.tour,name="tour"),
]
