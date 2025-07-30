from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


#Place router here
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')  # This handles full CRUD via /books/

# urls are listed below
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
     # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('api/token/', obtain_auth_token, name='api_token_auth'), # api token generation
]

   