from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.note_list, name='note_list'),
    url(r'^note/(?P<pk>\d+)/$', views.note_detail, name='note_detail'),
    url(r'^note/new/$', views.note_new, name='note_new'),
    url(r'^note/(?P<pk>\d+)/edit/$', views.note_edit, name='note_edit'),
    url(r'^note/(?P<pk>\d+)/delete/$', views.note_delete, name='note_delete'),
    url(r'^register/', views.register),
]