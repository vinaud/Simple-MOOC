from django.urls import path, re_path
from simplemooc.courses.views import index
from simplemooc.courses.views import details

app_name="courses"

urlpatterns = [
    path('', index, name='index'),
    re_path( r'^(?P<slug>[\w_-]+)/$', details, name='details')
   
]