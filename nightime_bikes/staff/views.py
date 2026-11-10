# Libreria para dividir los resultados en paginas
from django.core.paginator import Paginator
# Libreria para hacer busquedas con varias condiciones (O)
from django.db.models import Q
# get_object_or_404 busca un registro y da error 404 si no existe, redirect cambia de pagina y render muestra el template
from django.shortcuts import get_object_or_404, redirect, render

# Importacion de los formularios de la app staff
from .forms import EmpleadoForm, HorarioForm
# Importacion de la informacion de los modelos de staff
from .models import Empleado, Horario

# Create your views here.
# _________________________________________________
# Parte para las views de los empleados
# _________________________________________________

# Funcion para mostrar la lista de empleados, con busqueda y paginas
def lista_empleados(request):
    # Para obtener lo que el usuario escribio en el buscador (si no escribio nada queda vacio)
    query = request.GET.get('q', '').strip()

    # Para traer todos los empleados, los mas nuevos primero
    queryset = Empleado.objects.all().order_by('-id')

    # Condicional para filtrar solo si el usuario escribio algo en el buscador
    if query:
        # Busca el texto en el usuario o en la cedula (icontains no distingue mayusculas)
        queryset = queryset.filter(
            Q(usuario__icontains=query) | Q(cedula__icontains=query)
        )

    # Para dividir la lista en paginas de 5 empleados
    paginator = Paginator(queryset, 5)

    # Para obtener la pagina que el usuario esta viendo
    page_obj = paginator.get_page(request.GET.get('page'))

    # Para enviar al template la pagina, el texto buscado y el total de empleados
    contexto = {
        'page_obj': page_obj,
        'query': query,
        'total_registros': paginator.count,
    }
    return render(request, 'staff/lista_empleados.html', contexto)


# Funcion para mostrar la ficha completa de un empleado
def detalle_empleado(request, pk):
    # Para traer el empleado por su id (pk) o mostrar error 404 si no existe
    empleado = get_object_or_404(Empleado, pk=pk)

    # Para devolver el empleado al template
    return render(request, 'staff/detalle_empleado.html', {'empleado': empleado})


# Funcion para registrar un nuevo empleado
def crear_empleado(request):
    # Condicional para saber si el usuario envio el formulario (POST) o apenas va a abrirlo
    if request.method == 'POST':
        # Para llenar el formulario con los datos que el usuario escribio
        form = EmpleadoForm(request.POST)

        # Para verificar que los datos sean validos (cedula no repetida, campos obligatorios, etc.)
        if form.is_valid():
            # Para guardar el nuevo empleado en la base de datos
            form.save()

            # Para llevar al usuario a la lista de empleados
            return redirect('lista_empleados')
    else:
        # Si solo va a abrir la pagina, se muestra el formulario vacio
        form = EmpleadoForm()

    # Para mostrar el formulario, con el titulo y la pagina a la que vuelve el boton cancelar
    return render(request, 'staff/form_staff.html',
                  {'form': form, 'titulo': 'Registrar nuevo empleado', 'volver': 'lista_empleados'})


# Funcion para editar un empleado que ya existe
def editar_empleado(request, pk):
    # Para traer el empleado por su id (pk) o mostrar error 404 si no existe
    empleado = get_object_or_404(Empleado, pk=pk)

    # Condicional para saber si el usuario envio el formulario o apenas va a abrirlo
    if request.method == 'POST':
        # instance=empleado hace que se actualice el empleado y no se cree uno nuevo
        form = EmpleadoForm(request.POST, instance=empleado)

        # Para verificar que los datos sean validos
        if form.is_valid():
            # Para guardar los cambios en la base de datos
            form.save()

            # Para volver a la lista de empleados
            return redirect('lista_empleados')
    else:
        # Si solo va a abrir la pagina, se muestra el formulario con los datos actuales del empleado
        form = EmpleadoForm(instance=empleado)

    # Para mostrar el formulario con el nombre del empleado en el titulo
    return render(request, 'staff/form_staff.html',
                  {'form': form, 'titulo': f'Editar empleado: {empleado.usuario}', 'volver': 'lista_empleados'})


# _________________________________________________
# Parte para las views de los horarios
# _________________________________________________

# Funcion para mostrar la lista de horarios
def lista_horarios(request):
    # Para traer todos los horarios, los mas nuevos primero
    horarios = Horario.objects.all().order_by('-id')

    # Para enviar al template los horarios y cuantos hay
    contexto = {
        'horarios': horarios,
        'total_registros': horarios.count(),
    }
    return render(request, 'staff/lista_horarios.html', contexto)


# Funcion para registrar un nuevo horario
def crear_horario(request):
    # Condicional para saber si el usuario envio el formulario o apenas va a abrirlo
    if request.method == 'POST':
        # Para llenar el formulario con los datos que el usuario escribio
        form = HorarioForm(request.POST)

        # Para verificar que los datos sean validos
        if form.is_valid():
            # Para guardar el nuevo horario en la base de datos
            form.save()

            # Para llevar al usuario a la lista de horarios
            return redirect('lista_horarios')
    else:
        # Si solo va a abrir la pagina, se muestra el formulario vacio
        form = HorarioForm()

    # Para mostrar el formulario, con el titulo y la pagina a la que vuelve el boton cancelar
    return render(request, 'staff/form_staff.html',
                  {'form': form, 'titulo': 'Registrar nuevo horario', 'volver': 'lista_horarios'})


# Funcion para editar un horario que ya existe
def editar_horario(request, pk):
    # Para traer el horario por su id (pk) o mostrar error 404 si no existe
    horario = get_object_or_404(Horario, pk=pk)

    # Condicional para saber si el usuario envio el formulario o apenas va a abrirlo
    if request.method == 'POST':
        # instance=horario hace que se actualice el horario y no se cree uno nuevo
        form = HorarioForm(request.POST, instance=horario)

        # Para verificar que los datos sean validos
        if form.is_valid():
            # Para guardar los cambios en la base de datos
            form.save()

            # Para volver a la lista de horarios
            return redirect('lista_horarios')
    else:
        # Si solo va a abrir la pagina, se muestra el formulario con los datos actuales del horario
        form = HorarioForm(instance=horario)

    # Para mostrar el formulario con el nombre del horario en el titulo
    return render(request, 'staff/form_staff.html',
                  {'form': form, 'titulo': f'Editar horario: {horario.nombre_h}', 'volver': 'lista_horarios'})