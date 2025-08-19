from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token 
from rest_framework import generics, status, permissions, viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action


User = get_user_model()

#views here
#Registration views + token
class RegisterView(generics.CreateAPIView):
    '''Views for registeration'''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()   # calls RegisterSerializer.create()
        
        # create token
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


#Login + Token retrieval
class LoginView(APIView):
    '''Views to help login and manually retrieve token'''
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        print('We move')

        user = authenticate(username=username, password=password)
    
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def follow_user(self, request, pk=None):
        """Follow another user"""
        user_to_follow = self.get_object()
        if request.user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        user_to_follow.followers.add(request.user)  # keep followers updated

        return Response({"detail": f"You are now following {user_to_follow.username}."})

    @action(detail=True, methods=["post"])
    def unfollow_user(self, request, pk=None):
        """Unfollow another user"""
        user_to_unfollow = self.get_object()
        if request.user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        user_to_unfollow.followers.remove(request.user)

        return Response({"detail": f"You unfollowed {user_to_unfollow.username}."})