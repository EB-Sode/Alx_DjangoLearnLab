from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

#routers for the CRUD operations on books
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('', include(router.urls)),
]
