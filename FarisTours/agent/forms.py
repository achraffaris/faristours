from agent.models import Tour, TourDate, TourGallery
from django.forms import ModelForm


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = (
        'title',
        'subtitle',
        'price',
        'description',
        'duration',
        'is_top',
        'thumbnail',
        )

