from django.contrib import admin

from blog.models import Category, Post, Promotion


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Post, PostAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Promotion, PromotionAdmin)

