
import streamlit as st
import json

from tarefa import Tarefa
from estruturas.arvore_avl import ArvoreAVL


# ==========================================
# CONFIGURAÇÃO DA APLICAÇÃO
# ==========================================

st.set_page_config(
    page_title="Árvore de Tarefas",
    page_icon="🌳",
    layout="wide"
)

# Mantém a árvore entre as atualizações da página
if "arvore" not in st.session_state:
    st.session_state.arvore = ArvoreAVL()

if "proximo_id" not in st.session_state:
    st.session_state.proximo_id = 1

arvore = st.session_state.arvore


# ==========================================
# FUNÇÃO PARA DESENHAR A ÁRVORE AVL
# ==========================================

def gerar_grafico(no):
    if no is None:
        return None

    linhas = [
        "digraph AVL {",
        'graph [rankdir=TB, bgcolor="transparent"];',
        'node [shape=box, style="rounded,filled", '
        'fillcolor="#DCEBFA", color="#2878B5", '
        'fontname="Arial", fontsize=10];',
        'edge [color="#78909C"];'
    ]

    def percorrer(atual):
        if atual is None:
            return

        identificador = f"n{atual.tarefa.identificador}"

        nome = atual.tarefa.nome.replace("\n", " ")
        rotulo = (
            f"ID: {atual.tarefa.identificador}\\n"
            f"{nome}\\n"
            f"Prioridade: {atual.tarefa.prioridade}\\n"
            f"Altura: {atual.altura}"
        )

        linhas.append(
            f'{identificador} [label={json.dumps(rotulo)}];'
        )

        if atual.esquerda is not None:
            filho = f"n{atual.esquerda.tarefa.identificador}"
            linhas.append(f"{identificador} -> {filho};")
            percorrer(atual.esquerda)

        if atual.direita is not None:
            filho = f"n{atual.direita.tarefa.identificador}"
            linhas.append(f"{identificador} -> {filho};")
            percorrer(atual.direita)

    percorrer(no)

    linhas.append("}")

    return "\n".join(linhas)


# ==========================================
# CABEÇALHO
# ==========================================

st.title("🌳 TaskTree AVL")

st.caption(
    "Gerenciador de tarefas utilizando "
    "Árvore Binária de Busca Balanceada (AVL)."
)

st.divider()


# ==========================================
# INDICADORES
# ==========================================

tarefas = arvore.em_ordem()
total = arvore.quantidade()
prioritaria = arvore.maior_prioridade()

altura = arvore.altura(arvore.raiz)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de tarefas", total)
col2.metric(
    "Maior prioridade",
    prioritaria.prioridade if prioritaria else "-"
)
col3.metric(
    "Altura da árvore",
    altura
)
col4.metric(
    "Status",
    "Ativa" if total > 0 else "Vazia"
)

st.divider()


# ==========================================
# ABAS DA APLICAÇÃO
# ==========================================

aba1, aba2, aba3, aba4 = st.tabs([
    "📋 Tarefas",
    "➕ Cadastrar",
    "⚙️ Gerenciar",
    "🌳 Árvore AVL"
])


# ==========================================
# ABA 1 - LISTAR TAREFAS
# ==========================================

with aba1:

    st.subheader("Tarefas cadastradas")

    if tarefas:

        for tarefa in tarefas:

            with st.container(border=True):

                col1, col2 = st.columns([4, 1])

                with col1:
                    st.markdown(f"**{tarefa.nome}**")
                    st.write(tarefa.descricao)
                    st.caption(f"Identificador: {tarefa.identificador}")

                with col2:
                    st.metric(
                        "Prioridade",
                        tarefa.prioridade
                    )

        st.caption(
            "As tarefas estão apresentadas em ordem crescente "
            "de prioridade."
        )

    else:
        st.info("Nenhuma tarefa cadastrada ainda.")


# ==========================================
# ABA 2 - CADASTRAR TAREFA
# ==========================================

with aba2:

    st.subheader("Cadastrar nova tarefa")

    with st.form("form_cadastro"):

        nome = st.text_input("Nome da tarefa")

        descricao = st.text_area("Descrição")

        prioridade = st.select_slider(
            "Prioridade",
            options=[1, 2, 3, 4, 5],
            value=3
        )

        enviar = st.form_submit_button(
            "Cadastrar tarefa",
            use_container_width=True
        )

        if enviar:

            if not nome.strip():
                st.error("Informe o nome da tarefa.")

            else:

                nova_tarefa = Tarefa(
                    st.session_state.proximo_id,
                    nome.strip(),
                    descricao.strip(),
                    prioridade
                )

                arvore.inserir(nova_tarefa)

                st.session_state.proximo_id += 1

                st.success("Tarefa cadastrada com sucesso!")


# ==========================================
# ABA 3 - GERENCIAR TAREFAS
# ==========================================

with aba3:

    st.subheader("Buscar tarefa")

    id_busca = st.number_input(
        "Informe o ID da tarefa",
        min_value=1,
        step=1,
        key="id_busca"
    )

    if st.button("Buscar tarefa"):

        encontrada = arvore.buscar(id_busca)

        if encontrada:

            st.success("Tarefa encontrada!")

            st.write(f"**Nome:** {encontrada.nome}")
            st.write(f"**Descrição:** {encontrada.descricao}")
            st.write(f"**Prioridade:** {encontrada.prioridade}")

        else:
            st.warning("Tarefa não encontrada.")

    st.divider()

    st.subheader("Atualizar prioridade")

    with st.form("form_atualizar"):

        id_atualizar = st.number_input(
            "ID da tarefa",
            min_value=1,
            step=1,
            key="id_atualizar"
        )

        nova_prioridade = st.select_slider(
            "Nova prioridade",
            options=[1, 2, 3, 4, 5],
            value=3,
            key="nova_prioridade"
        )

        atualizar = st.form_submit_button(
            "Atualizar prioridade"
        )

        if atualizar:

            resultado = arvore.atualizar_prioridade(
                id_atualizar,
                nova_prioridade
            )

            if resultado:
                st.success("Prioridade atualizada!")
            else:
                st.error("Tarefa não encontrada.")

    st.divider()

    st.subheader("Remover tarefa")

    with st.form("form_remover"):

        id_remover = st.number_input(
            "ID da tarefa para remover",
            min_value=1,
            step=1,
            key="id_remover"
        )

        remover = st.form_submit_button(
            "Remover tarefa"
        )

        if remover:

            resultado = arvore.remover(id_remover)

            if resultado:
                st.success("Tarefa removida com sucesso!")
            else:
                st.error("Tarefa não encontrada.")


# ==========================================
# ABA 4 - VISUALIZAÇÃO DA ÁRVORE
# ==========================================

with aba4:

    st.subheader("Estrutura da Árvore AVL")

    st.write(
        "A árvore é organizada pela prioridade e pelo ID. "
        "Os nós à direita possuem chaves maiores."
    )

    if arvore.raiz is not None:

        grafico = gerar_grafico(arvore.raiz)

        st.graphviz_chart(
            grafico,
            use_container_width=True
        )

        st.divider()

        st.subheader("Informações da árvore")

        st.write(
            f"**Raiz:** {arvore.raiz.tarefa.nome}"
        )

        st.write(
            f"**Altura:** {arvore.altura(arvore.raiz)}"
        )

        st.write(
            f"**Quantidade de nós:** {arvore.quantidade()}"
        )

    else:

        st.info(
            "Cadastre algumas tarefas para visualizar a árvore AVL."
        )


# ==========================================
# RODAPÉ
# ==========================================

st.divider()

st.caption(
    "TaskTree AVL | Projeto de Estrutura de Dados e Algoritmos 2"
)
