
from django.conf.urls import include, url
from django.contrib import admin
import quadratic.urls
import web_application.urls
import book.urls
import fibonacci.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic', include(quadratic.urls)),
    url(r'^visual', include(book.urls)),
    url(r'^fibonacci/', include(fibonacci.urls)),
    url(r'^$', include(web_application.urls)),
    url(r'', include(web_application.urls)),
]
