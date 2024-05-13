# proje_dizininiz/urls.py

from django.contrib import admin
from django.urls import path, include  # include'ı ekleyin
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # blog.urls'i dahil edin
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
