from django.shortcuts import render
#from django.views.generic import ListView
from .models import items
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    homeChoice=items.Compo_CHOICES

    context={
        'homeChoice': homeChoice
    }
    return render(request, 'home.htm', context) 

@login_required
def details(request, Component_Type):
    Items=items.objects.filter(Component_Type=Component_Type)
    print(Items)

    context={
        'Items': Items
    }
    return render(request, 'details.htm', context) 

