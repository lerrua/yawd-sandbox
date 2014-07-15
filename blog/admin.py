from django.contrib import admin
from yawdadmin import admin_site

from .models import Post


class PostAdmin(admin.ModelAdmin):
    pass


admin_site.register(Post, PostAdmin)
