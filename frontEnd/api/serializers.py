from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password', 'email']
    
    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        ) 
        user.set_password(self.validated_data["password"])
        user.save()
        return user