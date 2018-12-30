from . import views
from django.conf.urls  import *
from django.contrib.auth import views as v
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index')
]