from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^create', views.create, name='create'),
    url(r'^(?P<id>\d+)$', views.show, name='show'),
    url(r'^(?P<id>\d+)/delete$', views.delete, name='delete'),
    ]
