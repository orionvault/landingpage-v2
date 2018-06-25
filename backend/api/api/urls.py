from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from presale.views import PresaleViewSet
from event.views import WallpaperViewSet

admin.autodiscover()
admin.site.site_title = "OrionVault - Administration"
admin.site.site_header = "OrionVault - Administration"

router = routers.DefaultRouter()
router.register(r'presales', PresaleViewSet, base_name='presales')
router.register(r'wallpapers', WallpaperViewSet, base_name='wallpapers')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/docs/', include_docs_urls(title='API v1')),
    path('management/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
