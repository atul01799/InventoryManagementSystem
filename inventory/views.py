from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Supplier,inventory
# Create your views here.
from rest_framework import generics,filters
from .serializers import InventorySerializer
from django_filters.rest_framework import DjangoFilterBackend

def home(request):
    '''
    This function renders all the inventory value with thier Supplier name
    '''
    invt= inventory.objects.all()
    return render(request,"inventory.html",{"inventory":invt})

def inventory_view(request,id):
    '''
    This function renders the specific inventory value 
    '''
    print(inventory.objects.get(id=1))
    invt= inventory.objects.get(id=id)
    return render(request,"view.html",{"inventory":invt})


class InventoryViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or search or filter.
    """
    search_fields = ['name']
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['name']
    queryset = inventory.objects.all()
    serializer_class = InventorySerializer