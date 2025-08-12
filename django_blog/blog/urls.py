from django.urls import path 
from django.contrib.auth import views
from .views import CustomLoginView, CustomLogoutView, RegisterView, profile, ListPostView, CreatePostView, UpdatePostView, DetailPostView, DeletePostView
from django.views.generic import RedirectView



urlpatterns = [
    #inbuilt auth views
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name= 'logout'),

    # Custom user views
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),

    #Custom Post views
    path('posts/', ListPostView.as_view(), name='home'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('post/new/', CreatePostView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
]