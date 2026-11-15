
from tarefa import Tarefa
from estruturas.arvore_avl import ArvoreAVL

arvore = ArvoreAVL()
proximo_id = 1


def cadastrar_tarefa():
    global proximo_id

    print("\n--- CADASTRAR TAREFA ---")

    nome = input("Nome: ").strip()
    descricao = input("Descrição: ").strip()

    if not nome:
        print("O nome é obrigatório.")
        return

    try:
        prioridade = int(input("Prioridade (1 a 5): "))

        if prioridade < 1 or prioridade > 5:
            print("A prioridade deve ser de 1 a 5.")
            return

    except ValueError:
        print("Digite uma prioridade válida.")
        return

    tarefa = Tarefa(proximo_id, nome, descricao, prioridade)
    arvore.inserir(tarefa)

    print("Tarefa cadastrada com sucesso!")
    print("ID da tarefa:", proximo_id)

    proximo_id += 1


def buscar_tarefa():
    try:
        identificador = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        return

    tarefa = arvore.buscar(identificador)

    if tarefa:
        print("\nTarefa encontrada:")
        print(tarefa)
        print("Descrição:", tarefa.descricao)
    else:
        print("Tarefa não encontrada.")


def remover_tarefa():
    try:
        identificador = int(input("ID da tarefa que deseja remover: "))
    except ValueError:
        print("ID inválido.")
        return

    resultado = arvore.remover(identificador)

    if resultado:
        print("Tarefa removida com sucesso!")
    else:
        print("Tarefa não encontrada.")


def atualizar_prioridade():
    try:
        identificador = int(input("ID da tarefa: "))
        prioridade = int(input("Nova prioridade (1 a 5): "))

        if prioridade < 1 or prioridade > 5:
            print("A prioridade deve ser de 1 a 5.")
            return

    except ValueError:
        print("Digite valores numéricos válidos.")
        return

    resultado = arvore.atualizar_prioridade(
        identificador, prioridade
    )

    if resultado:
        print("Prioridade atualizada com sucesso!")
    else:
        print("Tarefa não encontrada.")


def listar_tarefas():
    tarefas = arvore.em_ordem()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n--- LISTA DE TAREFAS ---")

    for tarefa in tarefas:
        print(tarefa)


def consultar_prioritaria():
    tarefa = arvore.maior_prioridade()

    if tarefa:
        print("\n--- TAREFA MAIS PRIORITÁRIA ---")
        print(tarefa)
        print("Descrição:", tarefa.descricao)
    else:
        print("Não existem tarefas cadastradas.")


def quantidade_tarefas():
    print("Total de tarefas:", arvore.quantidade())


def menu():
    while True:
        print("\n========== TASKTREE AVL ==========")
        print("1 - Cadastrar tarefa")
        print("2 - Buscar tarefa")
        print("3 - Remover tarefa")
        print("4 - Atualizar prioridade")
        print("5 - Listar tarefas")
        print("6 - Consultar tarefa prioritária")
        print("7 - Quantidade de tarefas")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa()

        elif opcao == "2":
            buscar_tarefa()

        elif opcao == "3":
            remover_tarefa()

        elif opcao == "4":
            atualizar_prioridade()

        elif opcao == "5":
            listar_tarefas()

        elif opcao == "6":
            consultar_prioritaria()

        elif opcao == "7":
            quantidade_tarefas()

        elif opcao == "0":
            print("Encerrando o TaskTree AVL!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
