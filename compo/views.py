from django.shortcuts import render
from .models import items
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    Items=items.objects.all()[:10]

    context={
        'title':'components',
        'Items': Items
    }
    return render(request, 'home.htm', context) 

@login_required
def details(request, Network_ID):
    Items=items.objects.get(Network_ID=Network_ID )

    context={
        'title':'components',
        'Items': Items
    }
    return render(request, 'details.htm', context) 