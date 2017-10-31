from django.conf.urls import include, url
from . import views


urlpatterns = [

    url(r'^random/$', views.random, name="random"),
    url(r'^gallery/(?P<pk>\d+)/$', views.gallery, name='gallery'),
    url(r'^$', views.index, name='index'),
    url(r'^login', views.loginUser, name = "loginUser"),
    url(r'^registration', views.createUser, name ="createUser")
]
