import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture                        #a fixture é para não repetir código , só passamos como parametro o def resposta
def resposta(client, db):               #acessando o banco
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200    #código de sucesso


def test_formulario_presente(resposta):   #estamos esperando uma resposta da tag form
    assertContains(resposta, '<form')


def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')    #vendo se o botão salvar funciona


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 1', feita=False),
        Tarefa(nome='Tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas

@pytest.fixture
def lista_de_tarefas_feitas(db):
    tarefas = [
        Tarefa(nome='Tarefa 3', feita=True),
        Tarefa(nome='Tarefa 4', feita=True),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes, lista_de_tarefas_feitas):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_lista_de_tarefas_pendentes_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):   #aqui esta pegando a lista de tarefas pendentes
    for tarefa in lista_de_tarefas_pendentes:             #aqui esta separando as tarefas individualmente
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)        #e aqui esta confirmando se o nome das tarefas aparece

def test_lista_de_tarefas_feitas_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_feitas):       #aqui esta pegando a lista de tarefas feitas
    for tarefa in lista_de_tarefas_feitas:                                 #aqui esta separando as tarefas individualmente
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)          #e aqui esta confirmando os nomes das tarefas
