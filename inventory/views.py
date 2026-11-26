from django.shortcuts import render
from .models import Stock

def inventory_list(request):
    return render(request, 'inventory/list.html',
                  {'stocks': Stock.objects.all()})
