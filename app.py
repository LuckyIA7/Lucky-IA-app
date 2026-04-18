import streamlit as st
from PIL import Image
import os
import moviepy.editor as mp
from moviepy.editor import ImageClip

st.set_page_config(page_title="Lucky IA PRO", layout="centered")

st.title("🚀 Lucky IA PRO")

# Produto
produto = st.text_input("📦 Qual produto vamos vender?")

# Estilo
estilo = st.selectbox(
    "🎬 Escolha o estilo do vídeo:",
    ["TikTok Viral", "Review", "Unboxing", "Estético"]
)

# Upload da foto
foto = st.file_uploader(
    "📸 Envie a foto do produto",
    type=["png", "jpg", "jpeg"]
)

# Gerar conteúdo
if st.button("🚀 Gerar Conteúdo PRO"):

    if foto is not None:

        # salvar imagem
        image = Image.open(foto)
        image_path = "produto.jpg"
        image.save(image_path)

        st.success("Imagem recebida!")

        # criar vídeo com zoom leve (efeito profissional)
        clip = ImageClip(image_path, duration=6)

        clip = clip.resize(lambda t: 1 + 0.04*t)

        video_path = "video_lucky.mp4"

        clip.write_videofile(
            video_path,
            fps=24,
            codec="libx264",
            audio=False
        )

        st.success("✅ Vídeo criado!")

        # botão download
        with open(video_path, "rb") as file:
            st.download_button(
                label="⬇️ Baixar Vídeo",
                data=file,
                file_name="lucky_video.mp4",
                mime="video/mp4"
            )

    else:
        st.warning("Envie uma foto primeiro.")
