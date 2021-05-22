from django.db import models
from django.db.models.deletion import CASCADE
from django_quill.fields import QuillField

from django.utils.text import slugify
from datetime import datetime

class Tour(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    slug = models.SlugField(null=True,blank=True)
    duration = models.PositiveIntegerField(default=1)
    created_at = models.DateField(auto_now_add=True,null=True)
    is_top = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="Thumbnails",default="1.jpg")
    description = QuillField()
    feedbacks = models.IntegerField(default=0)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tour, self).save(*args, **kwargs)

class Feedback(models.Model):
    tour = models.ForeignKey("Tour",on_delete=CASCADE)
    stars = models.PositiveIntegerField(default=0,max_length=5)
    review = models.TextField()
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    published = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{0} stars by {0}".format(self.star,self.name) 
    

class TourGallery(models.Model):
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallerry",null=True,blank=True)

class TourDate(models.Model):
    seats = models.PositiveIntegerField(default=1)
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date.strftime("%d %B, %Y"))  #str() convert datetime to a string
                                                    #strftime change datetime format :D

        
class BookingOrders(models.Model):
    booking_status_choices = [
        ('ok','confirmed'),
        ('ko','canceled'),
        ('pg','pending')
    ]
    planning = models.ForeignKey("TourDate",on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    payment = models.ForeignKey("Payment",on_delete=models.CASCADE,related_name='+',null=True,blank=True)
    status = models.CharField(max_length=2,choices=booking_status_choices,default="pg") #initial status after submission is Pending (pg) 
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "id: {} created at: {}".format(self.id,self.created_date.strftime("%d %B, %Y"))
    

class Payment(models.Model):
    payment_status = [
        ('ok','PAID'),
        ('ko','UNPAID'),
    ]
    booking = models.ForeignKey("BookingOrders", on_delete=models.CASCADE,related_name='+')
    session_id = models.CharField(max_length=400)
    status = models.CharField(max_length=2,choices=payment_status,default="ko")

