from django.urls import path, re_path
from django.contrib.auth.views import LoginView


app_name="accounts"

urlpatterns = [
    re_path(r'^entrar/$', LoginView.as_view(), {'template_name': 'accounts/login.html'},  name='login'),
    #r'^entrar/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'
    
   
]