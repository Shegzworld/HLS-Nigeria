from django.contrib import admin
from .models import Blog,Author,Comment,Category
# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = 'HLS Blog Portal'

blog_site = BlogAdminArea(name = 'Blog portal')

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)

blog_site.register(Blog)
blog_site.register(Author)
blog_site.register(Comment)
blog_site.register(Category)