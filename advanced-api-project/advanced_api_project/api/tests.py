from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

# Create your tests here.

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user and get token if needed
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Book endpoints
        self.book_list_url = reverse('book-list')  # name from urls.py
        self.book_detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_create_book(self):
        """Ensure we can create a new Book."""
        data = {
            "title": "Test Book",
            "author": self.author.id,
            "publication_year": 2023
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Test Book")

    def test_retrieve_book(self):
        """Ensure we can retrieve a single Book."""
        book = Book.objects.create(title="Book A", author=self.author, publication_year=2020)
        response = self.client.get(self.book_detail_url(book.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book A")

    def test_update_book(self):
        """Ensure we can update an existing Book."""
        book = Book.objects.create(title="Old Title", author=self.author, publication_year=2019)
        data = {
            "title": "Updated Title",
            "author": self.author.id,
            "publication_year": 2021
        }
        response = self.client.put(self.book_detail_url(book.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Updated Title")

    def test_delete_book(self):
        """Ensure we can delete a Book."""
        book = Book.objects.create(title="To Delete", author=self.author, publication_year=2018)
        response = self.client.delete(self.book_detail_url(book.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_authentication_required(self):
        """Ensure unauthenticated requests are blocked."""
        self.client.logout()
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # or 401 if using TokenAuth
