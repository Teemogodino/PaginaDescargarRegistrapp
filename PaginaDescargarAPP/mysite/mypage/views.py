from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'Main.html')
def cel(request):
    return render(request, 'Main-celular.html')

def homeProfe(request):
    return render(request, 'MainProfe.html')

def regAsistencia(request):
    profesor_name = request.session.get('profesor_name', 'Invitado') 
    asignaturas = Profesor.objects.get(nombre=profesor_name).materias.all()
    asignaturas = request.session.get('asignaturas', [])
    return render(request, 'RegistrarAsistencia.html', {
        'profesor_name': profesor_name,
        'Materias': asignaturas
    })
    

def login(request):

    if request.method == 'POST':
        correo = request.POST.get('correoP')  # Matching `correo_Inst` in your model
        contrasena = request.POST.get('contrasenaP')

    if request.method == 'POST':
        correo = request.POST.get('correoP')  # Matching `correo_Inst` in your model
        contrasena = request.POST.get('contrasenaP')

        try:
            # Fetch the professor based on the institutional email
            profesor = Profesor.objects.get(correo_Inst=correo)

            # Validate password using `check_password` for hashed passwords
            if contrasena == profesor.contrasena:
                request.session['profesor_name'] = profesor.nombre
                request.session['asignaturas'] = [materias.nombre_Materia for materias in profesor.materias.all()]
                messages.success(request, f'Bienvenido, {profesor.nombre}!')
                return redirect('homeProfe')  # Redirect to the home page (ensure the name is correct in your `urls.py`)
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Profesor.DoesNotExist:
            messages.error(request, 'Correo institucional no encontrado.')

    return render(request, 'login.html')


