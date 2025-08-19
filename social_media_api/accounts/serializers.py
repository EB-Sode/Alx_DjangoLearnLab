from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

#serializing models here
class UserSerializer(serializers.ModelSerializer):
    '''For displaying user info'''
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

#Register the users
class RegisterSerializer(serializers.ModelSerializer):
    '''For registeration'''
    password = serializers.CharField(write_only = True)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'bio', 'profilePicture', 'followers', 'password']

        def createUser(self, validated_data):
            followers = validated_data.pop("followers", [])
            user = CustomUser.objects.create_user(
                username = validated_data['username'],
                email = validated_data.get['email'],
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                bio = validated_data.get['bio'],
                profilePicture = validated_data.get ['profilePicture'],
                password = validated_data['password']
            )
            return user
        
#Login serializers
class LoginSerializer(serializers.ModelSerializer):
    '''For login after registration'''
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']