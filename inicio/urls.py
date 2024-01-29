

#from django.conf.urls import url

from django.urls import path 
from . import views 


urlpatterns = [ 
    path ("", views.inicio, name='inicio'),
    path('registrarUsuario', views.registrar, name='registrarUsuario'),

]