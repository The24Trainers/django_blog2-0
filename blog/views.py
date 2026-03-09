from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Category, Post

# Create your views here.


def category_list(request, category_id):
    post_by_category = Post.objects.filter(status="published" , category_id=category_id)
        
    get_category_id = get_object_or_404(Category, id=category_id)

    # try:
    #     get_category_id = Category.objects.get( id=category_id) 
    # except:
    #     return redirect('home')
    context = {
        'name': get_category_id,
        'post_by_category': post_by_category
    }
    return render(request, 'pages/single_category.html', context)