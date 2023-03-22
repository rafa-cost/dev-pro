from webdev.tarefas.models import Tarefa
from django.forms import ModelForm

class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'feita']