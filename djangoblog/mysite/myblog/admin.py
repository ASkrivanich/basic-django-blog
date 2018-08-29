from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

# admin.site.register(Post)
# admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created_date', 'modified_date', 'published_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
