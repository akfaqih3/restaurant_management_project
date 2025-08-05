from django.shortcuts import render
from .serializers import MenuSerializer 
from .models import Menu
from rest_framework.generics import ListAPIView


class MenuAPIView(ListAPIView):

    queryset = Menu.objects.all()
    fields = "__all__"
