from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Funcion que decide a donde va el usuario despues de hacer login
@login_required
def despues_login(request):
    # Si es administrador (superusuario o perfil con rol admin) va a la gestion
    if request.user.is_superuser or (hasattr(request.user, 'perfil') and request.user.perfil.rol == 'admin'):
        return redirect('lista_empleados')
    # Si es cliente va a la tienda
    return redirect('mostrar_productos')


# Funcion para registrar un usuario nuevo
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f'Cuenta creada para {usuario.username}. Ya puedes iniciar sesion.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registro.html', {'form': form})
