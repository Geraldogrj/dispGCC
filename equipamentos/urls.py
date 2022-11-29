from django.urls import path
from equipamentos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/<int:id>', views.home, name='home'),
    path('cadastrar/categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('ver_equipamento/<int:id>', views.ver_equipamento, name = "ver_equipamento"),
    path('', views.ver_esquadroes, name = "ver_esquadroes"),
    path('cadastrar/equipamento', views.cadastrar_equipamento, name = 'cadastrar_equipamento'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)