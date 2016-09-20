from django.conf.urls import include, url
from quadratic import views

urlpatterns = [
    url(r'$', views.index),
]