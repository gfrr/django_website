from django.conf.urls import url

from . import views

app_name = 'items'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<item_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<item_id>[0-9]+)/ask/$', views.ask, name='ask'),
]
