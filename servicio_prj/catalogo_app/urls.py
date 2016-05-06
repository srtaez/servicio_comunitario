from django.conf.urls import url
from catalogo_app.views import CatalogoView, CatalogoListView

urlpatterns = [
               url(r'^list/$', CatalogoListView.as_view(), name='catalogo_list'),
               url(r'^view/(?P<pk>\d+)/$', CatalogoView.as_view(), name='catalogo_view'),
              ]
