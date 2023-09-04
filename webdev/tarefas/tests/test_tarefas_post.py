import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tarefas.models import Tarefa

@pytest.fixture
def resposta(client, db):   #acessando o banco de dados
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})   #aqui estamos fazendo o teste de salvamento de tarefas(dados = nome : Tarefa), para ver se esta salvando com sucesso. É o contrario do codigo um pouco abaixo onde, esta salvando string vazia.
    return resp


def test_tarefa_existe_no_bd(resposta):                     #vendo se a tarefa existe no banco de dados
    assert Tarefa.objects.exists()

def test_redirecionamento_depois_do_salvamento(resposta):    #depois que salva a tarefa se ela esta sendo redirecionada , para o tarefa pendente
    assert resposta.status_code == 302


@pytest.fixture
def resposta_dado_invalido(client, db):     #acessando o banco
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})     #se o nome da tarefa for string vazia , sera um dado invalido
    return resp


def test_tarefa_não_existe_no_bd(resposta_dado_invalido):
    assert not Tarefa.objects.exists()                                 #afirmando que tarefa não existe


def test_pagina_com_dados_invalidos(resposta_dado_invalido):          #pagina com dados ivalidos , vai dar o codigo de erro 400
    assert resposta_dado_invalido.status_code == 400