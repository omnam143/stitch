from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from basic.models import Country, City
from django.utils import simplejson

import json


def indexOLD(request):
    #data = Country.objects.all()
    #countries = Country.objects.all()
    #countries_list = list(countries)
    countries_list = Country.objects.all().values_list('name', flat=True).order_by('name')
    list = "[["
    for item in countries_list:
        list = list + '"' + item + '",' 
    list = list + "]"
    list = [["Andorra","United Arab Emirates"]]
    #data = serializers.serialize("json", Country.objects.filter(name__startswith=alphabet))
    #return HttpResponse(data)
    #data = serializers.serialize("json", Country.objects.all())
    return HttpResponse(list)
    #return HttpResponse(json.dumps(data), content_type="application/json")

def index(request):
    data = Country.objects.values_list('name', flat=True).order_by('name')
    return HttpResponse(
        simplejson.dumps(list(data)),
        content_type = 'application/javascript'
    )

    
def ind(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('basic/typeaheadsimple.html', context_dict, context)

def landing(request):
    return HttpResponse("<b> OpenHealth : Here be the landing page</b>")
    
