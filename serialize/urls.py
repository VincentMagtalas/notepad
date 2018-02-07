from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^serialize/$', views.GenericNoteList.as_view(), name='serialize'),
    url(r'^serialize/(?P<pk>[0-9]+)/$', views.GenericNoteDetail.as_view(), name='snippets_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)