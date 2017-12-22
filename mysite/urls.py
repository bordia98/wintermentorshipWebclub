from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp import views as myappview
from mysite import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^myapp/$',myappview.home),
    url(r'^booklist/$',myappview.booklist),
]
