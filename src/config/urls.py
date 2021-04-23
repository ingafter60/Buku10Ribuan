# config/urls.py

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

# Import from app/ecommerce
from app.ecommerce import views
from app.ecommerce import admin_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', views.admin_login),

    # PAGE FOR ADMIN
    path('admin_home/',admin_views.admin_home)
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
