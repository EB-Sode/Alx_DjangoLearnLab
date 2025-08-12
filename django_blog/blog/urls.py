from django.urls import path 
from django.contrib.auth import views
from .views import CustomLoginView, CustomLogoutView, RegisterView, profile
from django.views.generic import RedirectView


urlpatterns = [
    #inbuilt auth views
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name= 'logout'),
    
    #custom views
    path('', RedirectView.as_view(url='login'), name= 'home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]