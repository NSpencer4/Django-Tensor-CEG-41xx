from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
#from django.conf.urls.media import media
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'ImgurClone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('Media.urls', namespace="Media")),

    url('^', include('django.contrib.auth.urls'))
]





urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
