from django.conf.urls import include, url
from book import views

urlpatterns = [
    url(r'book/buy/(?P<id>\d+)$', views.checkout),
    url(r'book/view/(?P<id>\d+)$', views.viewbook),
    url(r'football', views.football_index),
    url(r'book', views.index_book),
    url(r'phone', views.phone),
    url(r'login', views.login_index),
    url(r'$', views.index),
    url(r'/', views.myredirect),
]