from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def inicio(request, cuit):

    #Cuit = int(input("ingrese su cuit")) --> si uso el input no funciona acá. 
    diahoy = datetime.now() #---> no me funcionaba porque me faltaban los () y había puesto datetime.datetime

    bienvenidahoy = (f"Bienvenido <br> {cuit} a la Plataforma <br> Fecha de inicio: {diahoy}")

    return HttpResponse(bienvenidahoy)
    

def general(request):

    return HttpResponse('Listado de pólizas activas')


def template1(request):

    miHTML = open("C:/Users/joaco/Desktop/ProyectoPersonal/ProyectoURC/ProyectoURC/plantillas/template1urc.html")
#siempre se abre el archivo poniendo la dirección y cambiando la orientación de las barras \ por /
    plantilla = Template(miHTML.read())
#uso la función para leer la plantilla

    miHTML.close()
#cierro el archivo

    miContexto = Context() # hubo error en la importación de Context
#datos extra que vamos a agregar a la web

    documentoUrl = plantilla.render(miContexto)
#Con todo listo hacemos que funcione con el render. -> es la mezcla entre el contexto y el template. 

    return HttpResponse(documentoUrl)