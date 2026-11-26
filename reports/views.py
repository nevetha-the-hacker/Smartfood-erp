from django.shortcuts import render
from products.models import Product
from sales.models import Sale
from billing.models import Invoice

def report_dashboard(request):
    context = {
        'products': Product.objects.count(),
        'sales': Sale.objects.count(),
        'invoices': Invoice.objects.count(),
        'revenue': sum(s.amount for s in Sale.objects.all()),
    }
    return render(request, 'reports/dashboard.html', context)
