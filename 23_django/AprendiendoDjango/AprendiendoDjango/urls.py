"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
# Se importan las apps com mis propias vistas
from miapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('pagina-pruebas/', views.pagina, name="pagina"),
    path('pagina-pruebas/<int:redirigir>', views.pagina, name="pagina"), #Redirige la página si se pasa un parámetro
    path('admin/', admin.site.urls),
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name="contacto"), #La URL admiten los parámetros nombre y apellido
    path('contacto/<str:nombre>/', views.contacto, name="contacto"),
    path('contacto/', views.contacto, name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crar_articulo"),
    path('articulo', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editar_articulo, name="editar_articulo"),
    path('articulos/', views.articulos, name = "articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),
    path('save-article/', views.save_article, name="save"),
    path('create-article/', views.create_article, name="create"),
    path('create-full-article', views.create_full_article, name="create_full")
]

# Configuración para cargar imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)