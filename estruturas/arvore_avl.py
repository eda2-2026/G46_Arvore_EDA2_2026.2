class ArvoreAVL:

    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if no is None:
            return 0

        return (
            self.altura(no.esquerda)
            - self.altura(no.direita)
        )

    def atualizar_altura(self, no):
        no.altura = 1 + max(
            self.altura(no.esquerda),
            self.altura(no.direita)
        )

    def rotacao_direita(self, y):
        x = y.esquerda
        auxiliar = x.direita

        x.direita = y
        y.esquerda = auxiliar

        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        auxiliar = y.esquerda

        y.esquerda = x
        x.direita = auxiliar

        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y

    def balancear(self, no):
        self.atualizar_altura(no)

        fb = self.fator_balanceamento(no)

        # Caso LL
        if fb > 1 and self.fator_balanceamento(no.esquerda) >= 0:
            return self.rotacao_direita(no)

        # Caso LR
        if fb > 1 and self.fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # Caso RR
        if fb < -1 and self.fator_balanceamento(no.direita) <= 0:
            return self.rotacao_esquerda(no)

        # Caso RL
        if fb < -1 and self.fator_balanceamento(no.direita) > 0:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def chave(self, tarefa):
        return (tarefa.prioridade, tarefa.identificador)

    def inserir(self, tarefa):
        self.raiz = self._inserir(self.raiz, tarefa)

    def _inserir(self, no, tarefa):
        if no is None:
            from estruturas.no import No
            return No(tarefa)

        if self.chave(tarefa) < self.chave(no.tarefa):
            no.esquerda = self._inserir(no.esquerda, tarefa)
        elif self.chave(tarefa) > self.chave(no.tarefa):
            no.direita = self._inserir(no.direita, tarefa)
        else:
            return no

        return self.balancear(no)

    def buscar(self, identificador):
        return self._buscar(self.raiz, identificador)

    def _buscar(self, no, identificador):
        if no is None:
            return None

        if no.tarefa.identificador == identificador:
            return no.tarefa

        resultado = self._buscar(no.esquerda, identificador)

        if resultado is not None:
            return resultado

        return self._buscar(no.direita, identificador)

    def maior_prioridade(self):
        if self.raiz is None:
            return None

        atual = self.raiz

        while atual.direita is not None:
            atual = atual.direita

        return atual.tarefa

    def menor_prioridade(self):
        if self.raiz is None:
            return None

        atual = self.raiz

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual.tarefa

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is not None:
            self._em_ordem(no.esquerda, resultado)
            resultado.append(no.tarefa)
            self._em_ordem(no.direita, resultado)

    def quantidade(self):
        return len(self.em_ordem())