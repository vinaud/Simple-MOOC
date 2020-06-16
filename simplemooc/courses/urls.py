from django.urls import path
from simplemooc.courses.views import index
from simplemooc.courses.views import details

app_name="courses"

urlpatterns = [
    path('', index, name='index'),
    path( r'^(?P<slug>[\w_-]+)/$', details, name='details')
   
]