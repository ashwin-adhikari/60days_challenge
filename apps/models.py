from django.db import models


# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    quantity = models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return f"{self.name} {self.description} - {self.price} {self.quantity}"