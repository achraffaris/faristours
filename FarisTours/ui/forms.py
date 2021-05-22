from django.forms import ModelForm 

from agent.models import BookingOrders, Payment

class BookingOrderForm(ModelForm):
    class Meta:
        model = BookingOrders
        fields = (
            'full_name',
            'email',
            'phone',
            
        )
    