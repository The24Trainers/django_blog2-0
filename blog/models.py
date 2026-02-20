from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

status = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=status, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
