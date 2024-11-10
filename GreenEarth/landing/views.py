from django.shortcuts import render, redirect
from .models import Encuesta
from django.contrib import messages
from landing.forms import EncuestaForm
from . import forms
from django.db.models import Avg

def encuesta_view(request):
    form = forms.EncuestaForm()
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Encuesta enviada con éxito!')
            return render(request, 'encuesta.html', {'form': EncuestaForm()})
    data = {'form' : form}
    return render(request, 'encuesta.html',data)


def promedio_view(request):
    promedio_edad = Encuesta.objects.all().aggregate(Avg('edad'))['edad__avg']
    promedio_edad = int(promedio_edad) if promedio_edad is not None else 0


    contador = Encuesta.objects.filter(edad__gte=18, edad__lte=35).count()

    total_participantes = Encuesta.objects.count()

    total_true1 = Encuesta.objects.filter(pregunta1=True).count()
    total_false1 = Encuesta.objects.filter(pregunta1=False).count()


    total_true2 = Encuesta.objects.filter(pregunta2=True).count()
    total_false2 = Encuesta.objects.filter(pregunta2=False).count()


    total_true3 = Encuesta.objects.filter(pregunta3=True).count()
    total_false3 = Encuesta.objects.filter(pregunta3=False).count()


    porce_true1 = (total_true1 / total_participantes * 100) if total_participantes > 0 else 0
    porce_false1 = (total_false1 / total_participantes * 100) if total_participantes > 0 else 0


    porce_true2 = (total_true2 / total_participantes * 100) if total_participantes > 0 else 0
    porce_false2 = (total_false2 / total_participantes * 100) if total_participantes > 0 else 0


    porce_true3 = (total_true3 / total_participantes * 100) if total_participantes > 0 else 0
    porce_false3 = (total_false3 / total_participantes * 100) if total_participantes > 0 else 0


    return render(request, 'resultados.html', {
    'promedio_edad': promedio_edad,
    'contador': contador,
    'total_participantes': total_participantes,
    'porce_true1': porce_true1,
    'porce_false1': porce_false1,
    'porce_true2': porce_true2,
    'porce_false2': porce_false2,
    'porce_true3': porce_true3,
    'porce_false3': porce_false3
})
