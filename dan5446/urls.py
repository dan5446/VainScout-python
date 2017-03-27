from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf import settings
from api.urls import v1_api
from .views import Index

urlpatterns = patterns('',

    url(r'^$', login_required(Index.as_view()), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url('^activity/', include('actstream.urls')),
    url(r'^api/', include(v1_api.urls)),
    (r'^search/', include('haystack.urls')),

)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )