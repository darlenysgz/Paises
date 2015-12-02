from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^(?P<pk>[0-9]+)/resultados/$', views.Resultados.as_view(), name = 'resultados'),
    url(r'^(?P<id_pais>[0-9]+)/ciudades/$',views.ciudades, name = 'ciudades'),
]
