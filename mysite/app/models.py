import mongoengine
import datetime

class Students(mongoengine.Document):
	name = mongoengine.StringField(required=True)
	age = mongoengine.StringField(required=True)
	student_class = mongoengine.StringField(required=True)

class Attendance(mongoengine.Document):
	student_id = mongoengine.StringField(required=True)
	date = mongoengine.DateTimeField(default=datetime.datetime.now)

class Points(mongoengine.Document):
	student_id = mongoengine.StringField(required=True)
	points_obtained = mongoengine.StringField(required=True)
	date = mongoengine.DateTimeField(default=datetime.datetime.now)

class Behaviour(mongoengine.Document):
	behaviour_name = mongoengine.StringField(required=True)
	points = mongoengine.StringField(required=True)