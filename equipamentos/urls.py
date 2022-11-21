from django.urls import path
from equipamentos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('ver_equipamento/<int:id>', views.ver_equipamento, name = "ver_equipamento"),
    path('ver_esquadroes', views.ver_esquadroes, name = "ver_esquadroes")
] 