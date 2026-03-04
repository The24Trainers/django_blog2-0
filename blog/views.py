from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Category

# Create your views here.


def category_list(request, category_id):
    get_category_id = Category.objects.get( id=category_id) 
    context = {
        'name': get_category_id
    }
    return render(request, 'pages/single_category.html', context)