from django.urls import path, include
from .views import CommentViewSet, PostViewSet, FeedView, LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter


#router for CRUD operations
router = DefaultRouter()

router.register(r'post', PostViewSet, basename= 'post')
router.register(r"comment", CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name="feed"), 
    path("<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
]