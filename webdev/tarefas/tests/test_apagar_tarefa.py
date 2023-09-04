import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa(db):      #acessando o banco de dados
    return Tarefa.objects.create(nome='Tarefa 1', feita=False)   #consultando o banco de dados, e vendo que tarefa feita é igual a false


@pytest.fixture
def resposta(client, tarefa):   #
    resp = client.post(
        reverse('tarefas:apagar', kwargs={'tarefa_id': tarefa.id}),  #aqui postagem do cliente , revertida em aplicativo tarefas e views apagar, aplicatico tarefa_id igual a tarefa_id do html
    )
    return resp

def test_apagar_tarefa(resposta):
    assert not Tarefa.objects.exists()   #aqui esta confirmando se tarefa não existe

