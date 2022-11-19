from django.urls import path
from equipamentos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/categoria', views.cadastrar_categoria, name='cadastrar_categoria')
] 