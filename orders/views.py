from django.shortcuts import render
from .serializers import MenuSerializer 
from .models import Menu
from rest_framework.generics import ListAPIView


class MenuApiView(ListAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

