from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('about/',about,name="about"),
]