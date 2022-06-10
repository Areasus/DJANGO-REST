from django.http import JsonResponse
from .serializers import *
from .models import Drink

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def drink_list(request):
    drinks = Drink.objects.all()
    serialixer =DrinkSerializer(drinks,many=True)
    context ={
        "drinklist":serialixer.data
    }
    # return JsonResponse(context)
    return Response(serialixer.data)

@api_view(['GET'])
def fruits(request):
    fruits = Items.objects.all()
    serialixer =FruitsSerializer(fruits,many=True)
    context ={
        "drinklist":serialixer.data
    }
    return Response(serialixer.data)

@api_view(['POST'])
def drink_add(request):
    recieved_data = DrinkSerializer(data=request.data)
    if recieved_data.is_valid():
        recieved_data.save()
        return Response(recieved_data.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
    try:
        target = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        ser = DrinkSerializer(target)
        return Response(ser.data)

    if request.method == 'PUT':
        ser = DrinkSerializer(target,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        target.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
