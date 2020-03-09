from rest_framework.generics import ListAPIView ,CreateAPIView
from accounts.models import person
from django.contrib.auth.models import  User
from .serializers import userserializer,usercreateserializer ,profilecreateserializer

class userlistserializer(ListAPIView):
    queryset = person.objects.all()
    serializer_class = userserializer


class createuserserializer(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = usercreateserializer

class createprofileserializer(CreateAPIView):
    queryset = person.objects.all()
    serializer_class = profilecreateserializer