


from django.shortcuts import render
from blog.models import Category, Post, Promotion


def home(request):
    category = Category.objects.all()
    featured_blog_post = Post.objects.filter(is_feated=True)
    promotionData = Promotion.objects.all()

    context = {
        'category': category,
        'featured_blog_post' : featured_blog_post,
        'promotionData': promotionData
    }
    return render(request, 'index.html', context)