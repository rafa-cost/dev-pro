import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa_pendente(db): #acessando o banco de dados
    return Tarefa.objects.create(nome='Tarefa 1', feita=False)     #consultando no banco de dados , que a tarefa que não foi feita é pendente


@pytest.fixture
def resposta_com_tarefa_pendente(client, tarefa_pendente):
    resp = client.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_pendente.id}),
        data={'feita': 'true', 'nome': f'{tarefa_pendente.nome}-editada'}    # aqui é a questão de editar o nome da tarefa pedente, e também a questão de tornala uma tarefa feita "'feita': 'true'"
    )
    return resp


def test_status_code(resposta_com_tarefa_pendente):           #aqui o teste de tarefa feita , virar tarefa pendente
    assert resposta_com_tarefa_pendente.status_code == 302


def test_tarefa_feita(resposta_com_tarefa_pendente):        #aqui é o tarefa pendente virar o tarefa feita
    assert Tarefa.objects.first().feita

@pytest.fixture
def tarefa_feita(db):                                          #acessando o banco de dados
    return Tarefa.objects.create(nome='Tarefa 1', feita=True)   #acessando a tabela Tarefa e verificando se Tarefa1 , feita é igual a verdadeira


@pytest.fixture
def resposta_com_tarefa_feita(client, tarefa_feita):            # pega tarefa feita como parametro
    resp = client.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_feita.id}),  #aplicativo tarefas + detalhe views, comparando tarefa_id de html com tarefa_feita,id
        data={'nome': f'{tarefa_feita.nome}-editada'}                                #aqui é a questão de editar o nome da tarefa feita
    )
    return resp



def test_tarefa_pedentes(resposta_com_tarefa_feita):
    assert not Tarefa.objects.first().feita           #afirmar que tarefa primeira não foi feita
