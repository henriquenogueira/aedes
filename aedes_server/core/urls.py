from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clusters/$', views.clusters, name='clusters'),
    url(r'^latest/$', views.latest, name='latest'),
]
