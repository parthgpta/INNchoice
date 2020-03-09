from django.urls import  path
from . import views

urlpatterns = [
    path('listusers' , views.userlistserializer.as_view(),name= 'list'),
    path('listusers/create/signup' , views.createuserserializer.as_view(),name= 'create_signup'),
    path('listusers/create/profile' , views.createprofileserializer.as_view(),name= 'create_profile'),

]