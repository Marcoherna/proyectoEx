from django.urls import path
from . import views


urlpatterns = [
    path('indice', views.indice, name='indice'),
    path('crud', views.crud, name='crud'),
    path('trabajadoresAdd', views.trabajadoresAdd, name='trabajadoresAdd'),
    path('trabajadores_del/<str:pk>', views.trabajadores_del, name='trabajadores_del'),

   ]