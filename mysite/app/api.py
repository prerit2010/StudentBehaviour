from tastypie import authorization
from tastypie_mongoengine import resources
from models import *

class StudentsResource(resources.MongoEngineResource):
	class Meta:
		queryset = Students.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "students"
		authorization = authorization.Authorization()

class BehaviourResource(resources.MongoEngineResource):
	class Meta:
		queryset = Behaviour.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "behaviour"
		authorization = authorization.Authorization()

class AttendanceResource(resources.MongoEngineResource):
	class Meta:
		queryset = Attendance.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "attendance"
		authorization = authorization.Authorization()

class PointsResource(resources.MongoEngineResource):
	class Meta:
		queryset = Points.objects.all()
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		resource_name = "points"
		authorization = authorization.Authorization()