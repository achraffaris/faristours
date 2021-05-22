from django.urls import path 
from . import views

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('tours',views.tours,name="tours"),
    path('planning',views.tours_dates,name="tours_dates"),
    path('tours/add',views.add_tour,name="add_tour"),
    path('tours/update/<int:id>/',views.update_tour,name="update_tour"),
    path('delete_tour/<int:id>/',views.delete_tour,name="delete_tour"),
    path('orders',views.orders,name="orders"),
    path('blogs',views.blogs,name="blogs"),
    path('pages',views.pages,name="pages"),
    path('settings',views.settings,name="settings"),

]
