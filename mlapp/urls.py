from django.contrib import admin
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

 
urlpatterns = [
   
    path('', Index_Data.as_view(), name="index_url"),
    path('confirmation', Confirmation.as_view(), name="confirmation_url"),

]
