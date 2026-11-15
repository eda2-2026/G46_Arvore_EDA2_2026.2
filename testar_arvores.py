from tarefa import Tarefa
from estruturas.arvore_avl import ArvoreAVL

arvore = ArvoreAVL()

tarefas = [
    Tarefa(1, "Estudar Python", "Revisar conteúdo", 3),
    Tarefa(2, "Entregar trabalho", "Trabalho de EDA2", 5),
    Tarefa(3, "Responder e-mails", "E-mails pendentes", 1),
    Tarefa(4, "Fazer exercícios", "Lista de programação", 4),
]

for tarefa in tarefas:
    arvore.inserir(tarefa)

print("Tarefas antes da remoção:")
