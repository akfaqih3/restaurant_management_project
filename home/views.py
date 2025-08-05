from django.shortcuts import render
from orders.models import Menu
# Create your views here.

def home(request):
    menu = Menu.objects.all()
    return render(request, 'home.index', context={'menu':menu})
