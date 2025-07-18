from .views import list_books, LibraryDetailView
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    #path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # path('register/', views.Register.as_view(), name='register'),
    # Include the default auth URLs for login, logout, password management, etc.
    path('', include('django.contrib.auth.urls')),

    # Custom views for different user roles
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
]
