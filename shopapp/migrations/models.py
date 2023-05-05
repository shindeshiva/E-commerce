from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
 
class information(models.Model):
    Serialno = models.TextField(primary_key=True)
    Product = models.TextField()
    Quantityordered = models.TextField()
    Purchaseaddresss = models.TextField()
    City = models.TextField()

    def __str__(self):
        return f'{self.Serialno}, {self.Product}, {self.Quantityordered}, {self.Purchaseaddresss}, {self.City}'


class customerinfo(models.Model):
    Serialno = models.TextField(primary_key=True)
    Orderid = models.ForeignKey('shopapp.information', on_delete=models.CASCADE, related_name='values')
    Priceeach = models.TextField()
    Orderdate = models.TextField()
    Custid = models.TextField()

    def __str__(self):
        return f'{self.Serialno}, {self.Orderid}, {self.Priceeach}, {self.Orderdate}, {self.Custid}'