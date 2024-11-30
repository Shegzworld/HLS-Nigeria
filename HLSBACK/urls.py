from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.admin import blog_site
from NT_gallery.admin import store_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
    path('store/', store_site.urls),
    path('', include('home.urls')),
    path('user/', include('user.urls')),
    path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

    admin.site.index_title = 'HLS Nigeria'
    admin.site.site_header = 'Health and Lifestyle Serenity Network'
    admin.site.site_title = 'HLS Admin'
