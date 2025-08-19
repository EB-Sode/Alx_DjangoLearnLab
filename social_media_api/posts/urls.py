from django.urls import path, include
from .views import CommentViewSet, PostViewSet, FeedView
from rest_framework.routers import DefaultRouter


#router for CRUD operations
router = DefaultRouter()

router.register(r'post', PostViewSet, basename= 'post')
router.register(r"comment", CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name="feed"), 
]