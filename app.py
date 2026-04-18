import streamlit as st

# =============================
# CONFIGURAÇÃO DA PÁGINA
# =============================
st.set_page_config(
    page_title="Lucky IA",
    page_icon="✨",
    layout="wide"
)

# =============================
# SIDEBAR
# =============================
st.sidebar.title("✨ Lucky IA")
pagina = st.sidebar.radio(
    "Escolha o módulo:",
    [
        "🏠 Dashboard",
        "🎬 Roteiros",
        "📦 Produtos",
        "📅 Planejamento",
        "⚙️ Configurações"
    ]
)

# =============================
# DASHBOARD
# =============================
if pagina == "🏠 Dashboard":

    st.title("✨ Lucky IA - Painel Central")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Vídeos Postados", "12", "+3 hoje")

    with col2:
        st.metric("Produtos Testados", "5")

    with col3:
        st.metric("Vendas Estimadas", "R$ 420")

    st.divider()

    st.subheader("🔥 Missão do Dia")
    st.write("""
    ✅ Postar 3 vídeos  
    ✅ Testar 1 produto novo  
    ✅ Analisar comentários  
    """)

# =============================
# ROTEIROS
# =============================
elif pagina == "🎬 Roteiros":

    st.title("🎬 Gerador de Roteiros")

    produto = st.text_input("Nome do produto")
    nicho = st.selectbox(
        "Escolha o nicho",
        ["Beleza", "Casa", "Cozinha", "Tecnologia", "Fitness"]
    )

    if st.button("Gerar Roteiro"):

        roteiro = f"""
HOOK:
"Eu não sabia que precisava disso até testar..."

APRESENTAÇÃO:
Hoje testei o {produto} do nicho {nicho}.

PROBLEMA:
Todo mundo sofre com isso no dia a dia...

SOLUÇÃO:
Esse produto resolve rápido e sem esforço.

CTA:
Link no vídeo antes que acabe!
"""

        st.success("Roteiro criado!")
        st.text_area("Seu roteiro:", roteiro, height=300)

# =============================
# PROD
