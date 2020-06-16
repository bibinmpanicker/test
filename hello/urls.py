from django.conf.urls import url

from hello import views

urlpatterns = [
    # Urls for category file_type masters
    url(r'^hello_world_list/$', views.HelloWorldView.as_view({'get': 'list'})),
    url(r'^hello_world_add/$', views.HelloWorldView.as_view({'post': 'create'})),
    url(r'^hello_world_update/(?P<pk>\d+)/$', views.HelloWorldView.as_view({'patch': 'partial_update'})),
    url(r'^hello_world_details/(?P<pk>\d+)/$', views.HelloWorldView.as_view({'get': 'retrieve'})),
    url(r'^hello_world_delete/(?P<pk>\d+)/$', views.HelloWorldView.as_view({'delete': 'destroy'}))]
