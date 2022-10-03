from django.urls import path
from myl_app import views 

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('catalogo/',views.catalogo,name="catalogo"),
    path('promociones/',views.promociones,name="promociones"),
    path('sucursales/',views.sucursales,name="sucursales"),
    path('contactanos/',views.contactanos,name="contactanos"),
    path('ayuda/',views.ayuda,name="ayuda"),

]