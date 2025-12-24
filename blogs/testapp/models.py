from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # One-to-Many
    heading = models.CharField(max_length=255)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='blog_images/')  # Requires Pillow
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

