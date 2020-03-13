from django.urls import  path
from . import views

urlpatterns = [

    path('' , views.homepage , name='home'),
    #path('bookings/addtime' , views.addtime , name='addtime'),
    path('profile' , views.profile , name='profile'),
    path('deltime/<int:pk>',views.deltime , name='deltime'),
    path('add/day_adv',views.time_slots , name='time_slots'),
    path('add/specific/room' , views.add_specific , name = 'add_specific'),
    path('check' , views.check ),
    path('book_room/<int:pk>',views.book_room , name='book_room'),
    path('booked/details/<str:name>' , views.booked_room , name= 'booked_details'),
    path('del/book/<int:pk>' , views.delbook , name='delbook'),
    path('delete/room/available/<int:pk>' , views.available_room , name = 'del_available'),
    path('info/api', views.api_info , name='api_info')
    #path('add/available/' , views.addavailable , name='addavailable')

]