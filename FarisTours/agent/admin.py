from django.contrib import admin
from .models import Tour, TourGallery, TourDate, BookingOrders
# Register your models here.
admin.site.register(Tour)
admin.site.register(TourDate)
admin.site.register(BookingOrders)

admin.site.register(TourGallery)

