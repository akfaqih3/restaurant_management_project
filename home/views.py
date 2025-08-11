from django.shortcuts import render
from orders.models import Menu
from djanog.conf import settings


def home(request):
    menu = Menu.objects.all()
    context = {
        "menu":menu,
        "APP_NAME":settings.APP_NAME
    }
    return render(request, 'home.html', context={'menu':menu})



def custom_404(request, exception):
    """
    This function to handle page not found error
    """
    return render(request,'404.html', status=404)




def about(request):
    return render(request,'about.html')