from django.contrib import admin

from blog.models import Category, Post

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    
admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)