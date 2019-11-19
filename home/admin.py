from django.contrib import admin
from .models import Post, Friends,Message,Tweet
# Register your models here.

admin.site.register(Friends)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Tweet)
