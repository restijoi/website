from django.conf.urls import include, url
from website.views import UserProfileDetailView, ProjectDetailView
from django.contrib import admin
admin.autodiscover()

import website.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', website.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/$', website.views.profile, name='profile'),
    url(r'^profile/(?P<slug>[^/]+)/$', UserProfileDetailView.as_view(), name="profile"),
    url(r'^(?P<slug>[^/]+)/$', ProjectDetailView.as_view(), name="project"),
]
