from django.conf.urls import include, url
from fibonacci import views

urlpatterns = [
    url(r'$', views.index),
]