from django.shortcuts import render
from django.http import HttpResponse


def production_list(request):
    return render(request, 'production/list.html')


def production_home(request):
    return HttpResponse("SmartFood ERP - Production Management")
