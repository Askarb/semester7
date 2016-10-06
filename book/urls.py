from django.conf.urls import include, url
from book import views

urlpatterns = [
    url(r'buy/(?P<id>\d+)', views.checkout),
    url(r'$', views.index),
]