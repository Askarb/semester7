from django.conf.urls import include, url
from book import views

urlpatterns = [
    url(r'buy/(?P<id>\d+)$', views.checkout),
    url(r'view/(?P<id>\d+)$', views.viewbook),
    url(r'^/$', views.index),
    url(r'/', views.myredirect),
]