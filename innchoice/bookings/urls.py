from django.urls import  path
from . import views

urlpatterns = [

    path('' , views.homepage , name='home'),
    path('bookings/addtime' , views.addtime , name='addtime'),
    path('profile' , views.profile , name='profile'),
    path('deltime/<int:pk>',views.deltime , name='deltime'),
    path('edit/<int:pk>' , views.edittime , name= 'edittime'),
    path('add/day_adv',views.days_adv , name='daysadv'),
    path('check' , views.check ),
    path('book_room/<int:pk>',views.book_room , name='book_room')
    #path('add/available/' , views.addavailable , name='addavailable')

]