from rest_framework import serializers
from django.contrib.auth.models import User as UserModel



class Userserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password','email')

    def create(self, Validated_data):
        return User.objects.create_user(**Validated_data)

    