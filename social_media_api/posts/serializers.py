from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()

#___User Serializers here___
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]  # show only safe info

# Comments serializer
class CommentSerializers(serializers.ModelSerializer):
    '''Display comments, author and id'''
    author = UserSerializer(read_only=True)  # Show user info instead of just id
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="author", write_only=True, required=False
    )

    class Meta:
        model = Comment
        fields = ["id", "title", "content", "author", "author_id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        '''Set author autmotically if request.user is available'''

        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data ['author'] = request.user
            
        return super().create(validated_data)
        
# __POST serializer here__
class PostSerializers(serializers.ModelSerializer):
    '''Display posts, author and id'''
    author = UserSerializer(read_only=True)  # Show user info instead of just id
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="author", write_only=True, required=False
    )
    comments = CommentSerializers(many = True, read_only = True) #nested comments

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "author_id", "comments", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        '''Set author autmotically if request.user is available'''

        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data ['author'] = request.user
            
        return super().create(validated_data)