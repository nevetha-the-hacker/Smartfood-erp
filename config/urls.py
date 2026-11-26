from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('inventory/', include('inventory.urls')),
    path('production/', include('production.urls')),
    path('sales/', include('sales.urls')),
    path('billing/', include('billing.urls')),
    path('reports/', include('reports.urls')),
]
