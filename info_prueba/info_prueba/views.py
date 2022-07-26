from django.shortcuts import render



def inicio(request):
    template_name ="inicio.html"
    usuario = {
        "nombre" : "maxi",
        "apellido" : "echaide"
    }
    ctx = {
        "user_dict" : usuario
    }
    return render(request, template_name,ctx)   