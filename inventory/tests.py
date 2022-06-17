from django.test import TestCase
from django import urls
import pytest

from inventory.models import Supplier, inventory
# Create your tests here.
class URLTests(TestCase):
    '''
    This class contains all three test cases
    '''
    def homepage(self):
        '''
        This function provide the test result of "\inventory" page
        '''
        response=self.client.get('/inventory')
        self.assertEqual(response.status_code,200)

    def inventory_view(self):
        '''
        This function provide the test result of "\inventory\<int:id>" page
        '''
        sup= Supplier.objects.create(name="Atul")
        invt= inventory.objects.create(name="Maths",description="MAths1",note="Maths book 1",stock=100,availability=True,supplier=sup)
        response=self.client.get('/inventory/1')
        self.assertEqual(response.status_code,200)

    def api(self):
        '''
        This function provide the test result of "api\inventory" page
        '''
        response=self.client.get('/api/inventory')
        self.assertEqual(response.status_code,200)

