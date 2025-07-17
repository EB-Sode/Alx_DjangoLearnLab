from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)

class Library(models.Model):
    name = models.CharField(150)
    books = models.ManyToManyField(Book, related_name='title')

class Librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(Library, related_name = 'name')

