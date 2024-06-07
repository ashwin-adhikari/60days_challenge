from rest_framework import serializers
from .models import Drink

# class DrinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Drink
#         fields = [ 'id','name','description',price]

class DrinkSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=10, decimal_places=2,default=0.0)

    def create(self,validate_data):
        return Drink.objects.create(**validate_data)