import streamlit as st

# Configurar a página
st.set_page_config(page_title="Procurador de Justiça", page_icon="⚖️")

# Título e subtítulo com estilo
st.markdown(
    """
    <style>
    .titulo {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #333; 
    }
    .subtitulo {
        font-size: 20px;
        text-align: center;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<p class="titulo">Quando serei Procurador de Justiça?</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">ML: regressão linear simples com os dados da Lista de Antiguidade de Jan de 2025</p>', unsafe_allow_html=True)


# Widget para o usuário inserir o ano com estilo
ano_ingresso = st.slider(
    "Ano de ingresso na carreira:",
    1975, 2030,
    value=1994,
    help="Arraste a barra para selecionar o ano de ingresso na carreira."
)

# Função para calcular o resultado
def calcular_resultado(ano):
    """
    Calcula o resultado com base no ano de ingresso.

    Args:
      ano: O ano de ingresso na carreira.

    Returns:
      O resultado do cálculo.
    """
    resultado = int(ano * 1.0987068177853268 - 2159.4368249111044 + ano)
    return resultado

# Calcula o resultado com o ano inserido pelo usuário
resultado = calcular_resultado(ano_ingresso)

# Exibe o resultado com destaque e estilo
st.markdown(
    f"""
    <style>
    .resultado {{
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #007bff; 
        padding: 20px;
        border: 2px dashed #007bff;
        border-radius: 10px;
    }}
    </style>
    <p class="resultado">Procurador de Justiça em: {resultado}</p>
    """,
    unsafe_allow_html=True,
)