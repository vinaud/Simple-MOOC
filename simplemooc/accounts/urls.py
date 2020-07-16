from django.urls import path, re_path
from django.contrib.auth.views import LoginView 
from django.contrib.auth import views 

from simplemooc.accounts.views import register


app_name="accounts"

urlpatterns = [
    re_path(r'^entrar/$', LoginView.as_view(), {'template_name': 'accounts/login.html'},  name='login'),
    re_path(r'^sair/$', views.logout, {'next_page': 'core:home'},  name='logout'),
    re_path(r'^cadastre-se/$', register,  name='register'),

]