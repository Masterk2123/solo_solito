from django.urls import path
from .views import home, poblar_bd, producto, tienda_producto, ficha_producto, contacto, registro, sesion, vehiculo, vehiculo_tienda, vehiculo_ficha

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id_producto>', producto, name="producto"),
    path('tienda_producto', tienda_producto, name="tienda_producto"),
    path('ficha_producto/<id_producto>', ficha_producto, name="ficha_producto"),
    path('contacto', contacto, name="contacto"),
    path('registro', registro, name="registro"),
    path('sesion', sesion, name="sesion"),
    path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),


]
