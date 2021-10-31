from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('show',views.show,name="show"),
    path('home',views.home,name="home"),
    path('home1',views.home1,name="home1"),
    path('requestaddress',views.requestaddress,name="requestaddress"),
    path('changeaddress',views.changeaddress,name="changeaddress"),
    
    
]