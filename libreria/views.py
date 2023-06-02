from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro, Libro2, Libro3, Libro4, Libro5, Libro6
from .forms import LibroForm, Libro2Form, Libro3Form, Libro4Form, Libro5Form, Libro6Form
from .forms import LoginForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
import os

# Create your views here.
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')
@login_required
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
#--------------------------------------------------------------------
@login_required
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {"libros": libros})
@login_required
def libros2(request):
    libros = Libro2.objects.all()
    return render(request, 'libros/index2.html', {"libros": libros})
@login_required
def libros3(request):
    libros = Libro3.objects.all()
    return render(request, 'libros/index3.html', {"libros": libros})
@login_required
def libros4(request):
    libros = Libro4.objects.all()
    return render(request, 'libros/index4.html', {"libros": libros})
@login_required
def libros5(request):
    libros = Libro5.objects.all()
    return render(request, 'libros/index5.html', {"libros": libros})
@login_required
def libros6(request):
    libros = Libro6.objects.all()
    return render(request, 'libros/index6.html', {"libros": libros})

#TABLA01 INFORMES EMITIDOS
@login_required
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})
@login_required
def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':

        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})
@login_required
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
@login_required
def descargar_archivo(request, id):

    objeto = Libro.objects.get(id=id)

    if objeto.archivo:
        # Obtén la ruta completa del archivo
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(objeto.archivo))

        # Abre el archivo en modo binario
        with open(ruta_archivo, 'rb') as archivo:
            # Configura la respuesta HTTP con el archivo adjunto
            response = HttpResponse(archivo.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{objeto.archivo.name}"'
            return response

    return HttpResponse("El archivo no existe.")

#TABLA02 INFORMES RECIBIDOS
@login_required
def crear2(request):
    formulario = Libro2Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros2')
    return render(request, 'libros/crear.html', {'formulario': formulario})
@login_required
def editar2(request, id):
    libro = Libro2.objects.get(id=id)
    formulario = Libro2Form(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros2')
    return render(request, 'libros/editar.html', {'formulario': formulario})
@login_required
def eliminar2(request, id):
    libro = Libro2.objects.get(id=id)
    libro.delete()
    return redirect('libros2')
@login_required
def descargar_archivo2(request, id):

    objeto = Libro2.objects.get(id=id)

    if objeto.archivo:
        # Obtén la ruta completa del archivo
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(objeto.archivo))

        # Abre el archivo en modo binario
        with open(ruta_archivo, 'rb') as archivo:
            # Configura la respuesta HTTP con el archivo adjunto
            response = HttpResponse(archivo.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{objeto.archivo.name}"'
            return response

    return HttpResponse("El archivo no existe.")

#TABLA03 solicitudes emitidas
@login_required
def crear3(request):
    formulario = Libro3Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros3')
    return render(request, 'libros/crear.html', {'formulario': formulario})
@login_required
def editar3(request, id):
    libro = Libro3.objects.get(id=id)
    formulario = Libro3Form(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros3')
    return render(request, 'libros/editar.html', {'formulario': formulario})
@login_required
def eliminar3(request, id):
    libro = Libro3.objects.get(id=id)
    libro.delete()
    return redirect('libros3')
@login_required
def descargar_archivo3(request, id):

    objeto = Libro3.objects.get(id=id)

    if objeto.archivo:
        # Obtén la ruta completa del archivo
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(objeto.archivo))

        # Abre el archivo en modo binario
        with open(ruta_archivo, 'rb') as archivo:
            # Configura la respuesta HTTP con el archivo adjunto
            response = HttpResponse(archivo.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{objeto.archivo.name}"'
            return response

    return HttpResponse("El archivo no existe.")

#TABLA04 SOLICITUDES RECIBIDAS
@login_required
def crear4(request):
    formulario = Libro4Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros4')
    return render(request, 'libros/crear.html', {'formulario': formulario})
@login_required
def editar4(request, id):
    libro = Libro4.objects.get(id=id)
    formulario = Libro4Form(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros4')
    return render(request, 'libros/editar.html', {'formulario': formulario})
@login_required
def eliminar4(request, id):
    libro = Libro4.objects.get(id=id)
    libro.delete()
    return redirect('libros4')
@login_required
def descargar_archivo4(request, id):

    objeto = Libro4.objects.get(id=id)

    if objeto.archivo:
        # Obtén la ruta completa del archivo
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(objeto.archivo))

        # Abre el archivo en modo binario
        with open(ruta_archivo, 'rb') as archivo:
            # Configura la respuesta HTTP con el archivo adjunto
            response = HttpResponse(archivo.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{objeto.archivo.name}"'
            return response

    return HttpResponse("El archivo no existe.")

#TABLA05 VACACIONES Y COMPENSACIONES
@login_required
def crear5(request):
    formulario = Libro5Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros5')
    return render(request, 'libros/crear.html', {'formulario': formulario})
@login_required
def editar5(request, id):
    libro = Libro5.objects.get(id=id)
    formulario = Libro5Form(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros5')
    return render(request, 'libros/editar.html', {'formulario': formulario})
@login_required
def eliminar5(request, id):
    libro = Libro5.objects.get(id=id)
    libro.delete()
    return redirect('libros5')
@login_required
def descargar_archivo5(request, id):

    objeto = Libro5.objects.get(id=id)

    if objeto.archivo:
        # Obtén la ruta completa del archivo
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, str(objeto.archivo))

        # Abre el archivo en modo binario
        with open(ruta_archivo, 'rb') as archivo:
            # Configura la respuesta HTTP con el archivo adjunto
            response = HttpResponse(archivo.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{objeto.archivo.name}"'
            return response

    return HttpResponse("El archivo no existe.")

#TABLA06 personal
@login_required
def crear6(request):
    formulario = Libro6Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros6')
    return render(request, 'libros/crear.html', {'formulario': formulario})
@login_required
def editar6(request, id):
    libro = Libro6.objects.get(id=id)
    formulario = Libro6Form(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros6')
    return render(request, 'libros/editar.html', {'formulario': formulario})
@login_required
def eliminar6(request, id):
    libro = Libro6.objects.get(id=id)
    libro.delete()
    return redirect('libros6')



#Iniciar sesion
def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                
                return redirect('inicio')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Usuario o contraseña inválido')
        return render(request,'users/login.html',{'form': form})
    

def sign_out(request):
    logout(request)
    messages.success(request,f'Saliste de la sesión.')
    return redirect('login')      