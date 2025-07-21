from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        permissions = (
            ("can_view_books", "Can view books"),
            ("can_add_books", "Can add books"),
            ("can_change_books", "Can change books"),
            ("can_delete_books", "Can delete books"),
        )

class Library(models.Model):
    name = models.CharField(150)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(Library, related_name = 'librarian', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, role='Member',
                    date_of_birth=None, profile_photo=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            role=role,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('role', 'Admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile')
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} - {self.role}"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()