from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from basic.models import Country, City

def index(request):
    #json_serializer = serializers.get_serializer("json")()
    #json_serializer.serialize(Country.objects.all(), ensure_ascii=False, stream=response)
    #data = serializers.serialize("json", Country.objects.all())
    #return HttpResponse(json_serializer)
    data = serializers.serialize("json", City.objects.all())
    return HttpResponse(data)

    
    

