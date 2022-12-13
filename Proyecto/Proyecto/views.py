import datetime

from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from django.template import loader


def curso(request):
    fecha = datetime.datetime.now()
    return render(request,"curso.html",{"now":fecha})

def saludo(request):
 nombre = "Juan"
 return render(request,"plantilla.html",{"nombre_persona":nombre})

def saludo_html(request):
    documento="""<html><body><h1>Hola a todos!</h1></body></html>"""
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego!")

def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(documento)

def calcular_edad(request,edad,agno):
    periodo=agno-2022
    edad_futura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años"%(agno,edad_futura)
    return HttpResponse(documento)    