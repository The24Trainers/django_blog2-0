from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True , null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


status_choices = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Post(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True , null=True, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices, default='draft')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    is_feated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Promotion(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title