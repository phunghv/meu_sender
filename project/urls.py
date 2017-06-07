from django.conf.urls import include, url
from django.contrib import admin
from welcome.views import HistoryList
from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sender/', include('welcome.urls')),
    url(r'^view/',HistoryList.as_view()),
]
