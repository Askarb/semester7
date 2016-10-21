
from django.conf.urls import include, url
from django.contrib import admin
import quadratic.urls
import web_application.urls
import book.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic', include(quadratic.urls)),
    url(r'^books', include(book.urls)),
    url(r'^$', include(web_application.urls)),
]
