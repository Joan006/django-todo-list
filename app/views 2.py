from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    # template = loader.get_template("app/index.html")
    db_data = Task.objects.all()
    # Lo mostrara como array
    context = {
        "db_data": db_data[::-1],
        "update" :None
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'app/index.html', context)
    # con render evitamos poner las importaciones comentadas


def insert(request):
    # Funcion que reliza la recoleccion de datos , y las mustra en pantalla al agergar las tareas
    try:
        task_subject = request.POST["subject"]
        task_description = request.POST["description"]
        if task_subject == "" or task_description == "":
            raise ValueError("La tarea no puede estar vacia")
        db_data = Task(subject=task_subject, description=task_description)
        db_data.save()
        # Es para volver a direccionar a la pag inde
        return HttpResponseRedirect(reverse("index"))
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("index"))

def update_form(request, task_id):
    db_data = Task.objects.all()
    db_data_only = Task.objects.get(pk=task_id)
    print(db_data_only)
    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    return render(request, "app/index.html", context)

def delete(request, task_id):
    db_data = Task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse("index"))
