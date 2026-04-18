import streamlit as st
from moviepy.editor import ImageClip
import tempfile
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Lucky IA PRO", layout="centered")

st.title("🚀 Lucky IA PRO")
st.write("Transforme fotos de produtos em vídeos prontos para Reels, TikTok e Shopee.")

# INPUT DO PRODUTO
produto = st.text_input("📦 Nome do produto")

# UPLOAD DA IMAGEM
imagem = st.file_uploader(
    "📸 Envie a foto do produto",
    type=["png", "jpg", "jpeg"]
)

# FUNÇÃO PARA CRIAR VÍDEO
def criar_video(imagem_file):

    temp_dir = tempfile.mkdtemp()

    caminho_imagem = os.path.join(temp_dir, "imagem.jpg")

    with open(caminho_imagem, "wb") as f:
        f.write(imagem_file.read())

    caminho_video = os.path.join(temp_dir, "video.mp4")

    clip = ImageClip(caminho_imagem)

    # duração do vídeo
    clip = clip.set_duration(5)

    # tamanho padrão vertical
    clip = clip.resize(height=1920)

    # centralizar no formato 9:16
    clip = clip.on_color(
        size=(1080, 1920),
        color=(0, 0, 0),
        pos=("center", "center")
    )

    clip.write_videofile(
        caminho_video,
        fps=24,
        codec="libx264",
        audio=False
    )

    return caminho_video


# BOTÃO GERAR VÍDEO
if st.button("🎬 Criar Vídeo"):

    if imagem is None:
        st.warning("Envie uma imagem primeiro.")
    else:
        with st.spinner("Lucky IA criando seu vídeo..."):

            video_path = criar_video(imagem)

            st.success("✅ Vídeo criado!")

            video_file = open(video_path, "rb")

            st.download_button(
                label="⬇️ Baixar vídeo",
                data=video_file,
                file_name="lucky_video.mp4",
                mime="video/mp4"
            )
