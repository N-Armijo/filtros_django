"""
URL configuration for ejemplo_9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from ejemplo_filtros.views import vista_ejemplo as filtro
from ejemplo_filtros.views import saludo
from ejemplo_filtros.views import lista_frutas as frutas
from ejemplo_filtros.views import lista_productos as productos
from ejemplo_filtros.views import lista_nombres as nombres

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', filtro, name='' ),
    path('saludo/', saludo, name='saludo' ),
    path('frutas/', frutas, name='frutas' ),
    path('productos/', productos, name='productos' ),
    path('nombres/', nombres, name='nombres' ),
]
