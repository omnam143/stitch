from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from basic.models import Country, City
import json


def index(request,alphabet):
    #data = serializers.serialize("json", Country.objects.filter(name__startswith=alphabet))
    #return HttpResponse(data)
    data = serializers.serialize("json", City.objects.all())
    return HttpResponse(data)
    #return HttpResponse(json.dumps(data), content_type="application/json")

    
def ind(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('basic/typeaheadsimple.html', context_dict, context)
    
