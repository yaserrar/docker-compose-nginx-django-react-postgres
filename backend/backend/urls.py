from django.contrib import admin
from django.urls import path, re_path
from .views import send_some_data, MediaAccessView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/test/", send_some_data),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += (re_path(r"^media/(?P<path>.*)", MediaAccessView.as_view(), name="media"),)
