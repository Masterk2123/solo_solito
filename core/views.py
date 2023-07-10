from django.shortcuts import redirect,render
from .models import Producto, Categoria, Vehiculo
from .forms import ProductoForm, VehiculoForm


# Creando las vistas.


def home(request):
    return render(request, "core/home.html")

def tienda_producto(request):
    data = {"list": Producto.objects.all().order_by('id_producto')}
    return render(request, "core/tienda_producto.html", data)

def ficha_producto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    data = {"producto":  producto}
    return render(request, "core/ficha_producto.html", data)

def producto(request, action, id_producto):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id_producto": id_producto}

    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡Producto agregado!"
                except:
                    data["mesg"] = "¡Error al agregar el producto!"

    elif action == 'upd':
        objeto = Producto.objects.get(id_producto=id_producto)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡Producto actualizado!"
        data["form"] = ProductoForm(instance=objeto)

    elif action == 'del':
        try:
            Producto.objects.get(id_producto=id_producto).delete()
            data["mesg"] = "¡Producto eliminado!"
            return redirect(producto, action='ins', id_producto = '-1')
        except:
            data["mesg"] = "¡Producto no existe!"

    data["list"] = Producto.objects.all().order_by('id_producto')
    return render(request, "core/producto.html", data)









def vehiculo_tienda(request):
    data = {"list": Vehiculo.objects.all().order_by('patente')}
    return render(request, "core/vehiculo_tienda.html", data)

def vehiculo_ficha(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    data = {"vehiculo":  vehiculo}
    return render(request, "core/ficha_producto.html", data)

def vehiculo(request, action, id):
    data = {"mesg": "", "form": VehiculoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = VehiculoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El vehículo fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos vehículos con la misma patente!"

    elif action == 'upd':
        objeto = Vehiculo.objects.get(patente=id)
        if request.method == "POST":
            form = VehiculoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El vehículo fue actualizado correctamente!"
        data["form"] = VehiculoForm(instance=objeto)

    elif action == 'del':
        try:
            Vehiculo.objects.get(patente=id).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(vehiculo, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El vehículo ya estaba eliminado!"





    data["list"] = Vehiculo.objects.all().order_by('patente')
    return render(request, "core/vehiculo.html", data)

def poblar_bd(request):
    Producto.objects.all().delete()
    Producto.objects.create(id_producto=1, producto='LLANTA ARO 14 587 4X100', detalles="LLANTA ARO 14 587 4X100 BLACK FACE MACHINED POWERCARS", imagen="images/CN839.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id_producto=2, producto='NEUMATICO 245/45ZR20', detalles="	NEUMATICO 245/45ZR20 KAPSEN S2000 103Y", imagen="images/LL0307-2.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id_producto=3, producto='SILICONE FREE DRESSING', detalles="Silicone Free Dressing de Meguiar es la opción ideal para los profesionales que buscan un acondicionador para neumáticos de alto rendimiento que se pueda usar en cualquier entorno sensible a la silicona.", imagen="images/D16101-1.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id_producto=4, producto='ESPACIADOR 6X135/6X139', detalles="ESPACIADOR 6X135/6X139", imagen="images/ACC61.jpg", categoria=Categoria.objects.get(idCategoria=1))
    return redirect(producto, action='ins', id_producto = '-1')

    Vehiculo.objects.create(patente="SCAR47", marca='Mustang', modelo="Mustang de 1970", imagen="images/mustang.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=2))
    Vehiculo.objects.create(patente="TIRO98", marca='Mercedes-Benz', modelo="Iron Bike de 1998", imagen="images/motoiron.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=3))
    Vehiculo.objects.create(patente="UVAM20", marca='Silver Plus', modelo="Silver de 2000", imagen="images/silver.jpg",servicio="Suspension y Direccion",detalle_servicio="arreglo", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(vehiculo, action='ins', id = '-1')


def contacto(request):
    return render(request, "core/contacto.html")

def sesion(request):
    return render(request, "core/sesion.html")

def registro(request):
    return render(request, "core/registro.html")
