from django.urls import path, re_path
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView

from simplemooc.accounts.views import register
from simplemooc.accounts.views import dashboard 
from simplemooc.accounts.views import edit
from simplemooc.accounts.views import edit_password


app_name="accounts"

urlpatterns = [
    re_path('', dashboard,  name='dashboard'),
    re_path(r'^entrar/$', LoginView.as_view(), {'template_name': 'accounts/login.html'},  name='login'),
    re_path(r'^sair/$', LogoutView.as_view(), {'next_page': 'core:home'},  name='logout'),
    re_path(r'^cadastre-se/$', register,  name='register'),
    re_path(r'^editar/$', edit,  name='edit'), 
    re_path(r'^editar-senha/$', edit_password,  name='edit_password'), 

]