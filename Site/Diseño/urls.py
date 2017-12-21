from django.conf.urls import url
from Diseño.views import InicioView


urlpatterns = [
    url(r'^$', InicioView.as_view(), name='inicio'),
]


