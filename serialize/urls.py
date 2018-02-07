from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^serialize/$', views.snippet_list, name='serialize'),
    url(r'^serialize/(?P<pk>[0-9]+)/$', views.snippet_detail, name='snippets_detail'),
]