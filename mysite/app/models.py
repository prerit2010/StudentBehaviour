from __future__ import unicode_literals
from django.db import models
from mongoengine import *

class User(document):
	student_id = StringField(required=True)
	name = StringField(required=True)
	age = StringField(required=True)
	student_class = StringField(required=True)

	def __unicode__(self):
		return "%s"%(self.name)

class Attendance(document):
	student_id = StringField(required=True)
	date = DateTimeField(default=datetime.datetime.now)

class Points(document):
	student_id = StringField(required=True)
	points_obtained = StringField(required=True)
	date = DateTimeField(default=datetime.datetime.now)

class Behaviour(document):
	behavious_name = StringField(required=True)
	points = StringField(required=True)

