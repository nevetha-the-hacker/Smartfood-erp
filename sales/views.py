from django.shortcuts import render
from .models import Sale

def sales_list(request):
    return render(request, 'sales/list.html',
                  {'sales': Sale.objects.all()})
