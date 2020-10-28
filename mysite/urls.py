from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from django.urls import path, re_path, include
from django.conf.urls.static import static

# from geonode.urls import urlpatterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('swk.urls')),
    path('map/',include('map.urls')),
    # url(r'^swk/',include('swk.urls')),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
