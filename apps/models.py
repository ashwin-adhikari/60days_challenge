from django.db import models

# Create your models here.
# class feature:
#     id: int
#     name: str
#     details: str
class feature(models.Model):
    #what this does is make feature a model and whenever we use this model we do not need id , it automatically creates id for attributes

    name= models.CharField(max_length=100)
    details= models.CharField(max_length=500)
