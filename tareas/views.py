from django.shortcuts import render, redirect
from .models import Tarea
from .form import TareaForm

def adjuntar(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
        form = TareaForm()
    return render(request, 'adjuntar.html', {'form': form})

def listar(request):
    tareas = Tarea.objects.all()
    return render(request, 'listar.html', {'tarea': tareas})