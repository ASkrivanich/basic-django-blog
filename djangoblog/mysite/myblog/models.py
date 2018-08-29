from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


''' Use this if want to add posts back into the category
    def display_posts(self):
        """Create a string for posts. Required to display posts in Admin."""
        return ', '.join(posts.content for posts in self.posts.all()[:2])

    display_posts.short_description = 'Post'
'''



