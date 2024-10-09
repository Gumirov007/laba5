from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cats import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cats/', include('cats.urls')),
    path('', views.index),  # Добавляем маршрут для главной страницы
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
