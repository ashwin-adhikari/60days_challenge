from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@api_view(['GET', 'POST']) #this is a decorator
def drink_list(request,format=None):
    if request.method == 'GET':
    
    #get all drinks
    #searilize the meaning make them into json
    #return json 

     drinks= Drink.objects.all()
     serializer= DrinkSerializer(drinks, many=True)
    # return JsonResponse(serializer.data, safe=False)
    #serializer.data produces list starts with [ ] brackets
    #to produce object we use below starts with { }brackets 
     return Response(serializer.data)
    if request.method == 'POST':
       serializer= DrinkSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
       

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
   
   try:
      #checking just to make sure its a valid request
      drink = Drink.objects.get(pk=id)
   except Drink.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

   if request.method == 'GET':
      serializer = DrinkSerializer(drink)
      return Response(serializer.data)
   elif request.method == 'PUT':
      serializer = DrinkSerializer(drink,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
   elif request.method == 'DELETE':
      drink.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
   


@csrf_exempt
def drink_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = DrinkSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'GET':
        name = request.GET.get('name')
        if name:
            try:
                drink = Drink.objects.get(name=name)
                serializer = DrinkSerializer(drink)
                return JsonResponse([serializer.data], safe=False)
            except Drink.DoesNotExist:
                return JsonResponse([], safe=False)
        else:
            drinks = Drink.objects.all()
            serializer = DrinkSerializer(drinks, many=True)
            return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=405)  # Method Not Allowed for other HTTP methods

# import logging

# logger = logging.getLogger(__name__)

@csrf_exempt
def add_quantity(request):
  if request.method == 'POST':
      try:
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
      #   logger.debug("Received data: %s", pythondata)
      #debugging


        drink_name = pythondata.get('name')
        quantity_to_add = pythondata.get('quantity', 0)

      #   if not Drink.objects.filter(name=drink_name).exists():
      #           return JsonResponse({'error': 'Drink not found'}, status=404)
            
        drink = Drink.objects.get(name=drink_name)
        drink.quantity += quantity_to_add
        drink.save()
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data)
      except Drink.DoesNotExist:
            return HttpResponse(status=404, content='Drink not found')
      except Exception as e:
            print("error",e)
            return HttpResponse(status=500, content='Internal Server Error')
    
  else:
        return HttpResponse(status=405) 
   


