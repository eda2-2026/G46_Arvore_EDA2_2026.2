class Tarefa:
    def __init__(self, identificador, nome, descricao, prioridade):
        self.identificador = identificador
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade

    def __str__(self):
        return (
            f"ID: {self.identificador} | "
            f"Tarefa: {self.nome} | "
            f"Prioridade: {self.prioridade}"
        )