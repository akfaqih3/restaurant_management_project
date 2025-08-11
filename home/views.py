from django.shortcuts import render
from orders.models import Menu
# Create your views here.

def home(request):
    menu = Menu.objects.all()
    return render(request, 'home.html', context={'menu':menu})


def custom_404(request, exception):
    return render(request,'404.html', status=404)