from django.urls import  path ,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.redir ),
    path('login/' , auth_views.LoginView.as_view() , name = 'login' ),
    path('logout/' , auth_views.LogoutView.as_view() ,{'next_page' :'/'},name='logout'),
    path('signup/' , views.signup , name='signup'),
    #path('' , views.homepage , name='home'),


]