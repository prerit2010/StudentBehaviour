from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.template import loader

def index(request):
    students_list = Students.objects.all()
    behaviour_list = Behaviour.objects.all()
    context = {"students_list" : students_list, "behaviour_list" : behaviour_list}
    # for a in students_list:
    #     print a['age']
    template = loader.get_template('app/index.html')
    # return HttpResponse("Hello")
    return HttpResponse(template.render(request))