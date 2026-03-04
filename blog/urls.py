from django.urls import include, path

from blog import views




urlpatterns = [
    path('<int:category_id>/', views.category_list, name='category_list'),
]