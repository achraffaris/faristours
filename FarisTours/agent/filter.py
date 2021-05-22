import django_filters


from .models import BookingOrders




class BookingOrdersFilter(django_filters.FilterSet):
    class Meta:
        model = BookingOrders
        fields = (
            'planning',
            'status',
        )
    