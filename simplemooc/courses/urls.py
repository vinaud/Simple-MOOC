from django.urls import path
from simplemooc.courses.views import home


app_name="core"

urlpatterns = [
    path('', home, name='home'),
   
]