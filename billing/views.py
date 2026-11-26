from django.shortcuts import render
from .models import Invoice

def invoice_list(request):
    return render(request, 'billing/list.html',
                  {'invoices': Invoice.objects.all()})
