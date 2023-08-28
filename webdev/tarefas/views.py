from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from webdev.tarefas.forms import TarefaNovaForm, TarefaForm
from django.urls import reverse

from webdev.tarefas.models import Tarefa


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)     #form=a tarefa nova
        if form.is_valid():                     #se formulario é valido, salva o formulario
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))  #retornar http redirect reverter em tarefas:home
        else:                                                      #outra
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()   #codições de tarefas_ pendentese e tarefas_feitas
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()
            return render(request, 'tarefas/home.html',
                          {'form': form, 'tarefas_pendentes': tarefas_pendentes, 'tarefas_feitas': tarefas_feitas, },
                          status=400)
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    return render(request, 'tarefas/home.html',
                  {'tarefas_pendentes': tarefas_pendentes, 'tarefas_feitas': tarefas_feitas, })


# Create your views here.

def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)   # variavel tarefa
        form = TarefaForm(request.POST, instance=tarefa)  #variavel form
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))


def apagar(request, tarefa_id):  # aqui esta deletando as tarefas ja concluidas
    if request.method == 'POST':
        Tarefa.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('tarefas:home'))
