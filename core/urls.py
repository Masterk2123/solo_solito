from django.urls import path
from .views import home, poblar_pro, producto, tienda_producto, ficha_producto, contacto, registro, sesion, vehiculo, vehiculo_tienda, vehiculo_ficha, poblar_ve

urlpatterns = [
    path('', home, name="home"),
    path('poblar_pro', poblar_pro, name="poblar_pro"),
    path('producto/<action>/<id_producto>', producto, name="producto"),
    path('tienda_producto', tienda_producto, name="tienda_producto"),
    path('ficha_producto/<id_producto>', ficha_producto, name="ficha_producto"),
    path('contacto', contacto, name="contacto"),
    path('registro', registro, name="registro"),
    path('sesion', sesion, name="sesion"),
    path('poblar_ve', poblar_ve, name="poblar_ve"),
    path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),


]
