import streamlit as st
import random

st.title("🤖 Lucky IA PRO")

# Entrada do produto
produto = st.text_input("🛍️ Qual produto vamos vender?")

# Escolha do estilo
estilo = st.selectbox(
    "🎬 Escolha o estilo do vídeo:",
    ["TikTok Viral", "Shopee Conversão", "Reels Autoridade"]
)

# Roteiros por estilo
roteiros = {
    "TikTok Viral": [
        f"Eu não esperava que esse {produto} fosse tão bom 😳",
        f"Testei o {produto} e agora entendi por que está viralizando!",
        f"Se você ainda não viu esse {produto}, você está atrasada 😱",
        f"Comprei o {produto} por curiosidade… e viciei!",
        f"O {produto} apareceu pra mim 10 vezes e resolvi testar."
    ],

    "Shopee Conversão": [
        f"Esse {produto} está com preço MUITO bom hoje na Shopee.",
        f"Se você estava procurando um {produto} barato e bom, achei esse aqui.",
        f"O custo-benefício desse {produto} vale demais.",
        f"Comprei o {produto} e chegou super rápido.",
        f"O {produto} está compensando muito pelo valor."
    ],

    "Reels Autoridade": [
        f"Depois de testar vários modelos, esse {produto} me surpreendeu.",
        f"Vou mostrar por que esse {produto} virou meu favorito.",
        f"O diferencial desse {produto} está nos detalhes.",
        f"Se você busca qualidade, esse {produto} merece atenção.",
        f"Minha opinião sincera depois de usar o {produto}."
    ]
}

# Legendas
legendas = [
    "Link na sacolinha 🛍️",
    "Corre antes que acabe!",
    "Achadinho do dia ✨",
    "Vale muito a pena testar!",
    "Salva esse vídeo pra não perder."
]

# Hashtags
hashtags = [
    "#achadinhos",
    "#shopee",
    "#tiktokshop",
    "#promoção",
    "#ofertas",
    "#comprasonline",
    "#achadinhosdodia"
]

# Botão gerar conteúdo
if st.button("🚀 Gerar Conteúdo PRO") and produto:

    roteiro = random.choice(roteiros[estilo])
    legenda = random.choice(legendas)
    tags = " ".join(random.sample(hashtags, 4))

    st.subheader("🎬 Roteiro")
    st.write(roteiro)

    st.subheader("📝 Legenda")
    st.write(legenda)

    st.subheader("🔥 Hashtags")
    st.write(tags) import streamlit as st
from moviepy.editor import *
from PIL import Image
import tempfile
import os

st.set_page_config(page_title="Lucky IA 🎬", layout="centered")

st.title("✨ Lucky IA - Criadora de Vídeos para Afiliados")

produto = st.text_input("Qual produto vamos vender?")

foto = st.file_uploader(
    "📦 Envie a foto do produto",
    type=["png", "jpg", "jpeg"]
)

if foto and produto:

    st.success("Imagem carregada!")

    # salvar imagem temporária
    temp_img = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    image = Image.open(foto)
    image.save(temp_img.name)

    st.image(image, caption="Produto selecionado")

    if st.button("🔥 Criar Vídeo Automático"):

        st.info("Lucky IA está criando seu vídeo...")

        # cria animação zoom
        clip = ImageClip(temp_img.name).set_duration(5)

        clip = clip.resize(lambda t: 1 + 0.05*t)  # efeito zoom

        texto = TextClip(
            f"{produto}",
            fontsize=70,
            color="white",
            font="Arial-Bold"
        ).set_position("center").set_duration(5)

        video = CompositeVideoClip([clip, texto])

        output_path = os.path.join(tempfile.gettempdir(), "video_lucky.mp4")

        video.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio=False
        )

        st.success("✅ Vídeo pronto!")

        with open(output_path, "rb") as file:
            st.download_button(
                label="📲 Baixar Vídeo",
                data=file,
                file_name="video_lucky.mp4",
                mime="video/mp4"
)


