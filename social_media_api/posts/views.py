from .serializers import PostSerializers, CommentSerializers
from rest_framework import viewsets, filters, permissions, status, generics
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorOrReadOnly
from .models import Post, Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from notifications.models import Notification


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


class FeedView(APIView):
    """Feed of posts from users the current user follows"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  

        # Get the list of users the current user follows
        following_users = user.following.all()

        # Filter posts by these users
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

        # Serialize posts
        serializer = PostSerializers(posts, many=True, context={"request": request})
        return Response(serializer.data)

# VIEWS FOR LIKE AND UNLIKE POSTS
class LikePostView(generics.GenericAPIView):
    '''View to like a post'''
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Generate notification for post owner
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(generics.GenericAPIView):
    '''View to unlike a post'''
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You haven’t liked this post."}, status=status.HTTP_400_BAD_REQUEST)