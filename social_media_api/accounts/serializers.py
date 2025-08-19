from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


#serializing models here
class UserSerializer(serializers.ModelSerializer):
    '''For displaying user info'''
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

#Register the users
class RegisterSerializer(serializers.ModelSerializer):
    '''For registeration'''
    password = serializers.CharField(write_only = True)
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers', 'password']

    def create(self, validated_data):
        #create user and set followers and token
        followers = validated_data.pop("followers", [])

        user = get_user_model().objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            bio = validated_data.get('bio', ''),
            profile_picture = validated_data.get ('profilePicture', None),
            password = validated_data['password']
        )
         # Set followers if provided
        if followers:
            user.followers.set(followers)

        # Create token for the new user
        Token.objects.create(user=user)

        return user
        
#Login serializers
class LoginSerializer(serializers.Serializer):
    '''For login after registration'''
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']