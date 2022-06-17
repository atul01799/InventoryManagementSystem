from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
    path('inventory', views.home, name='home'),
    path('inventory/<int:id>', views.inventory_view, name='inventory_view'),
    path('api/inventory',views.InventoryViewSet.as_view()),
    
]
