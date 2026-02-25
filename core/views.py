


from django.shortcuts import render
from blog.models import Category, Post


def home(request):
    category = Category.objects.all()
    featured_blog_post = Post.objects.filter(is_feated=True)

    context = {
        'category': category,
        'featured_blog_post' : featured_blog_post
    }
    return render(request, 'index.html', context)