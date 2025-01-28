from . import api	

from django.urls import path
urlpatterns = [
    path('empresas/', api.obtener_empresas, name="obtener_empresas"),

]