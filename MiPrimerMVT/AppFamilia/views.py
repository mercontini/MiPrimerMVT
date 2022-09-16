from django.shortcuts import render
from AppFamilia.models import Familia
from django.http import HttpResponse

# Create your views here.
def familia (request):
    persona1 = Familia(nombre = "Andres", nacimiento = "1964-05-09", edad = 58, profesion = "Contador", relacion = "Padre")

    persona1.save()

    persona2 = Familia(nombre = "Viviana", nacimiento = "1964-09-07", edad = 58, profesion = "Bioquimica", relacion = "Madre")

    persona2.save()

    persona3 = Familia(nombre = "Virginia", nacimiento = "1992-05-11", edad = 30, profesion = "Odontologa", relacion = "Hermana")

    persona3.save()

    persona4 = Familia(nombre = "Eugenia", nacimiento = "1996-07-25", edad = 26, profesion = "Medica", relacion = "Hermana")

    persona4.save()

    diccionario = {"persona1":persona1,"persona2":persona2,"persona3":persona3,"persona4":persona4}

    return render(request, "AppFamilia/mifamilia.html", context = diccionario)

    