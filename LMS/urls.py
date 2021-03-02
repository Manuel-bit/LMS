from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('Home.urls')),
    url(r'^profile/', include('Profiles.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
