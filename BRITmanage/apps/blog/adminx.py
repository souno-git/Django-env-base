import xadmin
from xadmin import views
from .models import BlogArt


class BlogAdmin(object):
    list_display = ['title', 'author', 'label', 'add_time']
    search_fields = ['title', 'author', 'label', 'add_time']
    list_filter = ['title', 'author', 'label', 'add_time']
    style_fields = {"content": "ueditor"}


xadmin.site.register(BlogArt, BlogAdmin)
