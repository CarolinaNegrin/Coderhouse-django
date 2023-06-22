from django.http import HttpResponse
from django.template import Context, Template

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
	return HttpResponse("<h1>Segunda vista</h1>")

def nombre(request, nombre, apellido=None):
	nombre = nombre.capitalize()
	apellido = apellido.capitalize()
	return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
	mi_html = open("./templates/template1.html", "r")
	mi_template = Template(mi_html.read())
	mi_html.close()
	mi_contexto = Context(mi_template)
	mi_documento = mi_template.render(mi_contexto)
	return HttpResponse(mi_documento)
