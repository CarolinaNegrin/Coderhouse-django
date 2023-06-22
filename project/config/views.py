from django.http import HttpResponse


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
	return HttpResponse("<h1>Segunda vista</h1>")

def nombre(request, nombre, apellido=None):
	nombre = nombre.capitalize()
	apellido = apellido.capitalize()
	return HttpResponse(f"{apellido}, {nombre}")