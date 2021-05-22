from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .forms import TourForm
from .models import Tour, TourDate, TourGallery, BookingOrders
from datetime import datetime
from .filter import BookingOrdersFilter
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request,"agent/dashboard.html")



#CRUD OPERATIONS FOR TOUR
@login_required(login_url='/accounts/login/')
def add_tour(request):
    form = TourForm()
    if request.method == 'POST':
        form = TourForm(request.POST or None, request.FILES or None)
        date_list = request.POST.get('dates')
        seats = request.POST.get('seats')
        dr = date_list.split(",") # transform that string to a list ex: '12,7,5' ==> ['12','7','5'] 
        images = request.FILES.getlist('images')
        if form.is_valid():
            try: 
                tour_instance = form.save()
                #save multi record & link it to the current instance
                for date in dr:
                    converted_date = datetime.strptime(date, "%d %B %Y").date() #convert the string to datetime 
                    TourDate.objects.create(seats=seats,tour=tour_instance,date=converted_date)
                for image in images:
                    TourGallery.objects.create(tour=tour_instance,image=image)
                return redirect(tours)
            except: 
                form = TourForm()
        else:
            form = TourForm()
        
    context =  {
        'form':form,
    }
    return render(request,"agent/add_tour.html",context)

@login_required(login_url='/accounts/login/')
def tours(request):
    tours = Tour.objects.all()
    paginator = Paginator(tours, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'tours':page_obj,
    }
    return render(request,"agent/tours.html",context)

@login_required(login_url='/accounts/login/')
def update_tour(request,id):
    tour = Tour.objects.get(id=id)
    form = TourForm(request.POST or None, request.FILES or None, instance=tour)
    if form.is_valid():
        form.save()
        return redirect(tours)
    else:
        form = TourForm(request.POST or None, request.FILES or None, instance=tour)
    context = {
        'form':form,
        'tour':tour
    }
    return render(request,"agent/update_tour.html",context)

@login_required(login_url='/accounts/login/')
def delete_tour(request,id):
    try:
        tour = Tour.objects.get(id=id)
        tour.delete()
        return redirect(tours)
    except:
        return redirect(tours)
    return render(request,"agent/tours.html",context)

#END OF CRUD OPERATIONS FOR TOUR
@login_required(login_url='/accounts/login/')
def tours_dates(request):
    tours_dates = TourDate.objects.all()
    context = {
        'tours_dates':tours_dates,
    }
    return render(request,"agent/tours_dates.html",context)



@login_required(login_url='/accounts/login/')
def orders(request):
    bookings_orders = BookingOrders.objects.all().order_by('-created_date')
    order_filter = BookingOrdersFilter(request.GET,queryset=bookings_orders)
    bookings_orders = order_filter.qs
    paginator = Paginator(bookings_orders, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'order_filter':order_filter
    }
    return render(request,"agent/orders.html",context)
    order_filter = BookingOrdersFilter(request.GET,queryset=bookings_orders)
    bookings_orders = order_filter.qs
    context = {
        'bookings_orders':bookings_orders,
        'order_filter':order_filter
    }
    return render(request,"agent/orders.html",context)

@login_required(login_url='/accounts/login/')
def blogs(request):
    return render(request,"agent/blogs.html")


@login_required(login_url='/accounts/login/')
def pages(request):
    return render(request,"agent/pages.html")
    
@login_required(login_url='/accounts/login/')
def settings(request):
    return render(request,"agent/settings.html")

