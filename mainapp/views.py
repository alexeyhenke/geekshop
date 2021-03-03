from datetime import datetime

from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
        'current_date': datetime.now(),
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Products',
        'current_date': datetime.now(),
    }
    return render(request, 'mainapp/products.html', context)
