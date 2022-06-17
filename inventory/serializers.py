from .models import inventory
from rest_framework import serializers


class InventorySerializer(serializers.ModelSerializer):
    '''
    This class contains the serializer values of invetory model
    '''
    supplier_name = serializers.CharField(source='supplier.name')
    class Meta:
        model = inventory
        fields = ['name', 'supplier_name', 'availability']