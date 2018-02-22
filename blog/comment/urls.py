from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'article/(?P<article_pk>\d+)/$',views.article_comment,name='article_comment')
]