from django.shortcuts import render, redirect
from agent.models import Tour, TourDate, TourGallery, BookingOrders, Feedback
from .forms import BookingOrderForm
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views import View
import datetime, stripe
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_exempt


stripe.api_key = settings.STRIPE_SECRET_KEY
STRIPE_WEBHOOk_KEY = "whsec_QqhNNdcJND2xLSfJucMySP3sr0hI6L11"


def home(request):
    top_tours = Tour.objects.filter(is_top=True)[:3]
    #this will dislay duplicated listing .. distinct method is working only with PostegresSQL
    #top_tours_gallery = TourGallery.objects.filter(tour__in=top_tours) #__in is usefull when you want to filter a lot of recors
    new_tours = Tour.objects.all().order_by('created_at')[:3][::-1] # [:3] means get last 3 record [::-1] used to reverse these records (des)
    #highly_rated_tours = Tour.objects.all().order_by('feedbacks')[:3] # get top last 3 record that currently have the highest feedback
    context = {
        'tours':top_tours,
        'new_tours':new_tours,
        #'highly_rated_tours':highly_rated_tours,
    }
    return render(request,"client/index.html",context)


def success(request):
    return render(request,"ui/success.html")

def canceled(request):
    return render(request,"ui/canceled.html")

def CreateCheckoutSessionView(request,slug):
    if request.is_ajax and request.method == "POST":
        tour = Tour.objects.get(slug=slug)
        DOMAIN_NAME = "{}://{}".format(request.scheme,request.get_host())
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        planning_id=request.POST.get('planning')
        try:

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': tour.price * 100,
                            'product_data': {
                                'name': "Tour: {}".format(tour.title),
                                'images': ["{}://{}{}".format(request.scheme,request.get_host(),tour.thumbnail.url)], #get full url of that thumbnail
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                metadata = {
                    'planning_id':planning_id,
                    'full_name':full_name,
                    'email':email,
                    'phone':phone
                },
                success_url=DOMAIN_NAME + '/success/',
                cancel_url=DOMAIN_NAME + '/cancel/',
            )
            return JsonResponse({
                'id': checkout_session.id
            })
        except:
            return JsonResponse({
                'error': 'Please check your information and try again'
            })

now = datetime.datetime.now()
def tour(request,slug):
    tour = Tour.objects.get(slug=slug)
    galleries = TourGallery.objects.filter(tour=tour)
    planning = TourDate.objects.filter(tour=tour)
    feedbacks = Feedback.objects.filter(tour=tour)
    form = BookingOrderForm()
    if request.method == "POST":
        form = BookingOrderForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            form = BookingOrderForm()
    context = {
        'tour':tour,
        'galleries':galleries,
        'form':form,
        'planning':planning,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'range':range(5),
        'feedbacks':feedbacks

    }
    return render(request,"client/tour.html",context)

def tours(request):
    context = {
        'range':range(5), #feedback 
    }
    return render(request,"client/tours.html",context)
    

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOk_KEY
    )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    # Passed signature verification
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        TourDate_instance = TourDate.objects.get(id=session["metadata"]["planning_id"])
        TourDate_instance.seats -= 1 
        TourDate_instance.save()
        form = BookingOrders(
                planning=TourDate_instance,
                full_name = session["metadata"]["full_name"],
                email = session["metadata"]["email"],
                phone = session["metadata"]["phone"],
                status = 'ok',
            )
        form.save()
        BookingOrder_instance = form.save()

    return HttpResponse(status=200)
