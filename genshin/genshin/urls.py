from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('main.urls')),
    path('', include('acc.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('gallery/', include('gallery.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
