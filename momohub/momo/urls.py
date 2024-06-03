
from django.urls import path
from . import views

urlpatterns = [

    path('',views.all_momo,name= 'all_momo'),


]

