from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base_page, name='base_page'),
    url(r'^charges/$',views.charges, name='charges'),
]