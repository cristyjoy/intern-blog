from django.contrib import admin
from .models import Post, Index, Category, Tags, Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Index)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comment)
