from .views import list_books, LibraryDetailView
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # path('register/', views.Register.as_view(), name='register'),
    
    # Include the default auth URLs for login, logout, password management, etc.
    path('', include('django.contrib.auth.urls')),

    # Custom views for different user roles
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    path('add_book/', views.create_book, name= 'add_book'),
    path('edit_book/', views.edit_book, name= 'edit_book'),
    path('delete_book/', views.delete_book, name= 'delete_book'),
]
