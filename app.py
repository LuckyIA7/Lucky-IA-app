import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Lucky IA PRO",
    page_icon="🚀",
    layout="centered"
)

# TÍTULO
st.title("🚀 Lucky IA PRO")

# INPUT PRODUTO
produto = st.text_input("📦 Qual produto vamos vender?")

# ESCOLHA ESTILO
estilo = st.selectbox(
    "🎬 Escolha o estilo do vídeo:",
    [
        "TikTok Viral",
        "Review Natural",
        "Oferta Explosiva",
        "Unboxing",
        "Dica Rápida"
    ]
)

# UPLOAD FOTO
foto = st.file_uploader(
    "📸 Envie a foto do produto",
    type=["png", "jpg", "jpeg"]
)

# MOSTRAR FOTO
if foto:
    st.image(foto, caption="Produto enviado", use_column_width=True)

# BOTÃO GERAR
if st.button("🚀 Gerar Conteúdo PRO"):

    if produto == "":
        st.warning("Digite o nome do produto primeiro.")
    else:

        st.success("Conteúdo gerado com sucesso!")

        roteiro = f"""
🎬 ROTEIRO LUCKY IA

Produto: {produto}
Estilo: {estilo}

🎯 Hook (0-2s):
"Eu não sabia que precisava disso até testar..."

🎯 Demonstração:
Mostre detalhes do produto, textura e uso real.

🎯 Benefício:
Explique por que esse produto facilita a vida.

🎯 CTA:
"Se apareceu pra você, aproveita porque tá viralizando!"
"""

        st.subheader("🧠 Roteiro Gerado")
        st.write(roteiro)

        hashtags = "#tiktokshop #achadinhos #viral #compras #promoção"

        st.subheader("🔥 Hashtags")
        st.write(hashtags)
