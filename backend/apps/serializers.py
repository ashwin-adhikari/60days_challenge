from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    quantity = serializers.DecimalField(max_digits=10,decimal_places=0,default=0)

    def create(self,validate_data):
        return Drink.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

    
    # #object validation
    # def validate(self, data):
    #     value1 = data.get('quantity')
    #     value2 = data.get('price')
    #     if value1 > 50:
    #         raise serializers.ValidationError('You\'ve achieved discount')
    #     return data
    

    # # Field level validation
    
    # def validate_quantity(self,value):
    #     if value > 50:
    #      raise serializers.ValidationError('You\'ve achieved a discount.')
    #     return value


        
    


