from django.conf.urls import include, url
from django.contrib import admin
from app.api import StudentsResource

student_resource  = StudentsResource()

urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(student_resource.urls))
]