from django.shortcuts import render
from equipos.models import equipo
from django.views.generic import TemplateView


def inicio(request):
    template_name ="inicio.html"
    equipos = equipo.objects.all()
    print (equipos)
    equipo.objects.create(nombre = "Alemania")
        
    


    ctx = {
        "equipos" : equipos
    }
    return render(request, template_name,ctx)   
"""
def login(request):
    template_name = "login.html"
    return render(request, template_name, {})
"""

# vistas basadas en clases 

class Login (TemplateView):
    template_name= "login.html"
   