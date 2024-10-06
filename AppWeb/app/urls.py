from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultados/', views.mostrar_resultados, name='resultados'),
]
