from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model() #Inbuilt user

# Create your models here.
class Post(models.Model):
    '''Model representing a post'''
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'Poster')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else "Untitled Post"
    
class Comment(models.Model):
    '''Model representing a comment on a post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

class Like(models.Model):
    '''Model representing a like on a post'''
    post = models.ForeignKey(
        "Post", 
        on_delete=models.CASCADE, 
        related_name="likes"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "user")  # prevents duplicate likes
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"