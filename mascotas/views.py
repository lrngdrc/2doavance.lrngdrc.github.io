from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import razas

# Create your views here.

def Razas(request):
    # return HttpResponse('Nuestra primera vista!')
    misRazas = razas.objects.all().values()
    template = loader.get_template('modelitos.html')
    context = {
        'misRazas': misRazas,
    }
    return HttpResponse(template.render(context, request))

def Bienvenida(request):
    template = loader.get_template('bienvenida.html')
    return HttpResponse(template.render())

