from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
