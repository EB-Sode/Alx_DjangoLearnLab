from django.shortcuts import render
from .serializers import PostSerializers, CommentSerializers
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorOrReadOnly
from .models import Post, Comment


# Create your views here.
#API VIEWS FOR CRUD OPERATIONS

class PostViewSet(viewsets.ModelViewSet):
    '''CRUD for post'''
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializers
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

      # Filtering, Searching, Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["author"]   # e.g. ?author=2
    search_fields = ["title", "content"]  # e.g. ?search=django
    ordering_fields = ["created_at", "updated_at", "title"]  # ?ordering=title

    def perform_create(self, serializer):
        '''Assign logged in user as author'''
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    '''CRUD for comments'''
    queryset = Comment.objects.all().order_by=("-created_at")
    serializer_class = CommentSerializers
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Assign logged in user as author"""
        serializer.save(authur=self.request.user)
