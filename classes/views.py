from django.shortcuts import render
from django.http import HttpResponse
from classes.models import Turma
def home(request):
    lista_mat = Turma.objects.filter(turno='matutino')
    lista_vesp = Turma.objects.filter(turno='vespertino')
    lista_not = Turma.objects.filter(turno='noturno')
    context = {
        'lista_mat' : lista_mat,
        'lista_vesp' : lista_vesp,
        'lista_not' : lista_not,
    }
    return render(request, 'classes/index.html', context)
