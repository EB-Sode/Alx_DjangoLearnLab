from django.urls import path, include
from .views import BookList

# urls are listed below

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list')
]