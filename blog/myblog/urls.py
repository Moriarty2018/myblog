from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^article/(?P<pk>\d+)/$',views.detail,name='detail'),
    url(r'^guilei/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.guidang,name='guidang'),
    url(r'^category/(?P<pk>\d+)/$',views.category,name='category'),
]