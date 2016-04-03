# from tastypie.resources import Resource
from tastypie import authorization
from tastypie_mongoengine import resources
from models import *

class StudentsResource(resources.MongoEngineResource):
	class Meta:
		queryset = Students.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "students"

class BehaviourResource(resources.MongoEngineResource):
	class Meta:
		queryset = Behaviour.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "behaviour"

class AttendanceResource(resources.MongoEngineResource):
	class Meta:
		queryset = Attendance.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "attendance"

class PointsResource(resources.MongoEngineResource):
	class Meta:
		queryset = Points.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "points"