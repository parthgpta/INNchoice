from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import person

class userserializer(ModelSerializer):
    class Meta:
        model = person
        fields = [
            'user',
            'name',
            'gender',
            'dob',
            'phone',
            'user_type'
        ]

class profilecreateserializer(ModelSerializer):
    class Meta:
        model = person
        fields = [
            'user',
            'name',
            'gender',
            'dob',
            'phone',
            'user_type'
        ]

class usercreateserializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
