from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.template import loader

def index(request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(request))