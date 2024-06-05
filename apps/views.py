from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Drink
from .serializers import DrinkSerializer

# Create your views here.
def drink_list(request):
    #get all drinks
    #searilize the meaning make them into json
    #return json 

    drinks= Drink.objects.all()
    serializer= DrinkSerializer(drinks, many=True)
    # return JsonResponse(serializer.data, safe=False)
    #serializer.data produces list starts with [ ] brackets
#to produce object we use below starts with { }brackets 
    return JsonResponse({"drinks": serializer.data}, safe=False)


