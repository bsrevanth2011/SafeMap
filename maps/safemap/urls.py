from django.conf.urls import url
from . import views

app_name = 'safemap'

urlpatterns = [
    url(r'^$', views.details, name='detail'),
    url(r'^result$', views.results, name='result'),
]