from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.loginUser, name="loginUser"),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^registration', views.createUser, name="createUser"),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^gallery/(?P<pk>\d+)/$', views.gallery, name='gallery'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^test/', views.test, name='test'),
    url(r'^help/', views.help, name='help'),
]
