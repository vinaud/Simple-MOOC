from django.urls import path
from simplemooc.courses.views import index


app_name="core"

urlpatterns = [
    path('', index, name='index')
   
]