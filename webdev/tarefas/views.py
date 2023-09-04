from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from webdev.tarefas.forms import TarefaNovaForm, TarefaForm
from django.urls import reverse

from webdev.tarefas.models import Tarefa


def home(request):
    if request.method == 'POST':                                         # esse metodo ele publica, manda msg
        form = TarefaNovaForm(request.POST)                              #estamos acessando os dados de "TarefaNovaForm" atraves do request.POST e passando isso para a variavel form
        if form.is_valid():                                              #se formulario é valido, salva o formulario dentro do nosso banco de dados
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))        #retornar http redirect reverter em tarefas:home
        else:                                                           #outra
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()   #acessando no banco de dados as tarefas não feitas e passando para variavel "tarefas_pendentes"
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()       #acessando no banco de dados as tarefas feitas e passando para minha variavel "tarefas_feitas"
            return render(request, 'tarefas/home.html',       #aqui estamos reenderizando a informação para o template tarefas/home.html
                          {'form': form, 'tarefas_pendentes': tarefas_pendentes, 'tarefas_feitas': tarefas_feitas, },
                          status=400)                                     #aqui estamos ligando nossas variaveis com as do html, esse status 400 é código de erro caso o usuario tente salvar a tarefa com o campo em branco, ai ira aparecer uma msg de erro abaixo do campo. O form : form que passamos no contexto acima e não passamos no contexto abaixo, também é referente a msg de erro que, ele auxilia para mostrar a msg de erro {{ form.nome.errors }}
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()          #acessando no banco de dados as tarefas não feitas e passando para variavel "tarefas_pendentes"
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()              #acessando no banco de dados as tarefas feitas e passando para variavel "tarefas_feitas"
    return render(request, 'tarefas/home.html',
                  {'tarefas_pendentes': tarefas_pendentes, 'tarefas_feitas': tarefas_feitas, })


# Create your views here.

def detalhe(request, tarefa_id):                   #acho que eles colocaram tarefa_id como parametro na função pois, essa função e a de baixo recebem as tarefas, agora a função def home apenas cria a tarefa.
    if request.method == 'POST':                     #metodo pubiclar
        tarefa = Tarefa.objects.get(id=tarefa_id)   # variavel tarefa, buscando no banco de dados os id da tarefa que vamos editar
        form = TarefaForm(request.POST, instance=tarefa)  #variavel form, estamos passando o dicionario post com todos os dados "request.POST". E também vamos passar a instancia que vamos editar no caso tarefa
        if form.is_valid():                            # formulario é valido , salva o formulario
            form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))     #e redireciona para "tarefa:home" que é o nome da app + def home de veiw


def apagar(request, tarefa_id):
    if request.method == 'POST':                      #metodo pubiclar
        Tarefa.objects.filter(id=tarefa_id).delete()  # aqui esta deletando o id da tarefa, que automaticamente deleta a tarefa
    return HttpResponseRedirect(reverse('tarefas:home'))   #depois redireciona para tarefa:home
