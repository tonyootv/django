from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField()
    create_time = models.DateTimeField()
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time')

#admin.site.register(BlogPost, BlogPostAdmin)