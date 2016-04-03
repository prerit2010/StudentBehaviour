# from tastypie.resources import Resource
from tastypie import authorization
from tastypie_mongoengine import resources
from models import Students

class StudentsResource(resources.MongoEngineResource):
	class Meta:
		queryset = Students.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "students"



