from webdev.tarefas import views
from django.urls import path

app_name='tarefas'

urlpatterns=[
    path('', views.home, name='home'),
    path('<int:tarefa_id>', views.detalhe, name='detalhe'),  #<int:tarefa_id>aqui mostra que tarefa_id é um numero inteiro, parece que esta guardando a tarefa do view detalhe
    path('apagar/<int:tarefa_id>', views.apagar, name='apagar'), #aqui esta apagando
]
#aqui são os caminhos dentro do aplicativo tarefas, que estão detalhados em views