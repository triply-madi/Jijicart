from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.productname
