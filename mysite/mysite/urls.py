from django.conf.urls import include, url
from django.contrib import admin
from app.api import StudentsResource, BehaviourResource, AttendanceResource, PointsResource

student_resource  = StudentsResource()
behaviour_resource = BehaviourResource()
attendance_resource = AttendanceResource()
points_resource = PointsResource()

urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(student_resource.urls)),
    url(r'^api/', include(behaviour_resource.urls)),
    url(r'^api/', include(attendance_resource.urls)),
    url(r'^api/', include(points_resource.urls))
]