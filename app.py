import streamlit as st
from moviepy.editor import ImageClip
from PIL import Image
import tempfile
import os

st.set_page_config(page_title="Lucky IA PRO", layout="centered")

st.title("🚀 Lucky IA PRO")

produto = st.text_input("📦 Qual produto vamos vender?")

estilo = st.selectbox(
    "🎬 Escolha o estilo do vídeo:",
    ["TikTok Viral", "Review", "Oferta Relâmpago"]
)

imagem = st.file_uploader(
    "📸 Envie a foto do produto",
    type=["png", "jpg", "jpeg"]
)

# -------- FUNÇÃO DE CRIAR VIDEO --------
def criar_video(imagem_file):

    img = Image.open(imagem_file).convert("RGB")

    # salva imagem temporária
    temp_img = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    img.save(temp_img.name)

    # cria clip
    clip = ImageClip(temp_img.name)

    # duração do vídeo
    clip = clip.set_duration(5)

    # tamanho vertical TikTok
    clip = clip.resize(height=1920)

    # centraliza
    clip = clip.on_color(
        size=(1080,1920),
        color=(0,0,0),
        pos=("center","center")
    )

    # salva vídeo
    video_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name

    clip.write_videofile(
        video_path,
        fps=24,
        codec="libx264",
        audio=False
    )

    return video_path


# -------- BOTÃO --------
if st.button("🚀 Gerar Conteúdo PRO"):

    if imagem is None:
        st.warning("Envie uma imagem primeiro.")
    else:
        st.success("Criando vídeo...")

        video = criar_video(imagem)

        st.video(video)

        with open(video, "rb") as file:
            st.download_button(
                label="⬇️ Baixar Vídeo",
                data=file,
                file_name="lucky_video.mp4",
                mime="video/mp4"
            )
