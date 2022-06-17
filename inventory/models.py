from django.db import models

# Create your models here.

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name=name=models.CharField(max_length=200, null=False,default="", blank=False,verbose_name="Supplier Name")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = "Supplier"

class inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200, null=False,default="", blank=False,verbose_name="Name")
    description=models.CharField(max_length=200, null=False,default="", blank=False,verbose_name="Description")
    note=models.TextField(verbose_name="Note")
    stock=models.IntegerField(null=False,default=0, blank=False,verbose_name="Stock")
    availability=models.BooleanField(default=False,verbose_name="Availability")
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, related_name="Supplier")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = "Inventory"

