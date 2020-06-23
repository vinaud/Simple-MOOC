from django.urls import path, re_path
from django.contrib.auth.views import LoginView


app_name="accounts"

urlpatterns = [
    path(r'^entrar/$', LoginView, {'template_name': 'accounts/login.html'},  name='login'),
    
   
]