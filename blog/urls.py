# blog/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
