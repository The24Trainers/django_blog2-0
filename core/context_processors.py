from blog.models import Category



def category_list_processor(request):
    categories = Category.objects.all()
    return dict(categories=categories)