from django.urls import path
from . import views


urlpatterns = [
    path('indice', views.indice, name='indice'),
    path('crud', views.crud, name='crud'),
    path('trabajadoresAdd', views.trabajadoresAdd, name='trabajadoresAdd'),
    path('trabajadoresDel/<str:pk>', views.trabajadoresDel, name='trabajadoresDel'),
    path('trabajadoresFindEdit/<str:pk>', views.trabajadoresFindEdit, name='trabajadoresFindEdit'),
    path('trabajadoresUpdate', views.trabajadoresUpdate, name='trabajadoresUpdate'),

   ]