from django.urls import path
from blog import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('base/', views.base, name='base'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('otros/', views.otros, name='otros'),
    path('', views.inicio, name='inicio'),
    path('muro/', views.muro, name='muro'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editar/<int:id>/', views.editar, name='editar')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
