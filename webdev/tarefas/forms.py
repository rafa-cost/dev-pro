from webdev.tarefas.models import Tarefa
from django.forms import ModelForm
#acho que toda vez que utilizamos form (formulario) temos fazer esse modulo forms
class TarefaNovaForm(ModelForm): #com esse formulario nos vamos validar os dados e salvar no banco de dados
    class Meta:
        model = Tarefa           #importamos o model Tarefa
        fields = ['nome']        #esse formulario ele atribui o nome

class TarefaForm(ModelForm):     # esse formularo ira lidar com todos campos das tarefas, diferente do outro formulario acima
    class Meta:
        model = Tarefa
        fields = ['nome', 'feita']   # além do nome, aqui no caso para indicar se a tarefa foi feita ou não