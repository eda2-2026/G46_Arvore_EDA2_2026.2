# 🌳 TaskTree AVL — Gerenciador de Tarefas por Prioridade

O **TaskTree AVL** é uma aplicação web desenvolvida em Python que permite gerenciar tarefas de acordo com seus níveis de prioridade, utilizando uma **Árvore Binária de Busca Balanceada AVL** como estrutura principal de organização.

O projeto foi desenvolvido para a disciplina de Estrutura de Dados e Algoritmos 2 (EDA2), com o objetivo de aplicar na prática os conceitos de árvores binárias de busca, balanceamento e operações de inserção, busca e remoção.

## 🚀 Demonstração

**Acesse a aplicação:** [TaskTree AVL — Aplicação Web](https://g46arvoreeda220262-3zwszhx6drs4awb8372gun.streamlit.app)

## ✨ Funcionalidades

- **Cadastro de tarefas:** criação de tarefas com nome, descrição e prioridade.
- **Listagem de tarefas:** visualização das tarefas cadastradas em ordem crescente de prioridade.
- **Busca:** localização de tarefas por identificador.
- **Atualização de prioridade:** alteração da prioridade de uma tarefa, com reorganização da árvore.
- **Remoção:** exclusão de tarefas da estrutura AVL.
- **Consulta de maior prioridade:** identificação da tarefa mais prioritária.
- **Visualização gráfica:** representação da árvore AVL com seus nós e conexões.
- **Indicadores:** exibição da quantidade de tarefas e da altura da árvore.

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- Árvore Binária de Busca Balanceada AVL
- Graphviz
- Git e GitHub

## 🌳 Estrutura de dados: Árvore AVL

A aplicação utiliza uma Árvore AVL para organizar as tarefas com base em uma chave composta por prioridade e identificador:

`(prioridade, identificador)`

A estrutura mantém a propriedade de uma Árvore Binária de Busca e realiza rotações automaticamente quando necessário para preservar o balanceamento.

As operações implementadas incluem:

- Inserção de nós;
- Busca de tarefas;
- Remoção de nós;
- Atualização de prioridade;
- Percurso em ordem;
- Rotações simples e duplas.

### Complexidade das operações

| Operação | Complexidade |
|---|---|
| Inserção | O(log n) |
| Busca pela chave da árvore | O(log n) |
| Remoção | O(log n) |
| Consulta da maior prioridade | O(log n) |
| Listagem em ordem | O(n) |

A busca pelo identificador, na implementação atual, percorre a árvore, pois sua ordenação é baseada na prioridade e no identificador.

## 💻 Como executar localmente

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acessar a pasta do projeto

```bash
cd G46_Arvore_EDA2_2026.2
```

### 3. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 4. Ativar o ambiente virtual

No macOS ou Linux:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
streamlit run streamlit_app.py
```

A aplicação estará disponível no navegador, normalmente no endereço:

```text
http://localhost:8501
```

## 📁 Estrutura do projeto

```text
G46_Arvore_EDA2_2026.2/
│
├── estruturas/
│   ├── __init__.py
│   ├── no.py
│   └── arvore_avl.py
│
├── tarefa.py
├── app.py
├── streamlit_app.py
├── testar_arvores.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📚 Objetivo acadêmico

O desenvolvimento do TaskTree AVL permite compreender a importância das árvores binárias de busca balanceadas na organização e recuperação eficiente de informações.

O projeto demonstra como as rotações AVL mantêm a altura da árvore controlada, evitando que sua estrutura se torne excessivamente desbalanceada após operações de inserção e remoção.

## 👩‍💻 Projeto acadêmico

**Disciplina:** Estrutura de Dados e Algoritmos 2 (EDA2)

**Projeto:** Gerenciador de Tarefas por Prioridade utilizando Árvore AVL.

**Linguagem:** Python.
