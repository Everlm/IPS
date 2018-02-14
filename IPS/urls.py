from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url, patterns
from django.contrib import admin
from AreaOftalmologia.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IPS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('AreaOftalmologia.api.urls')),
    url(r'^token-auth/$','rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',IndexView.as_view()),
)
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

url(r'^admin/', include(admin.site.urls)),
