from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    url(r'^serialize/$', views.GenericNoteList.as_view(), name='serialize'),
    url(r'^serialize/(?P<pk>[0-9]+)/$', views.GenericNoteDetail.as_view(), name='snippets_detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]