import streamlit as st
from moviepy.editor import ImageClip
from PIL import Image
import tempfile

st.set_page_config(page_title="Lucky IA PRO", layout="centered")

st.title("🚀 Lucky IA PRO")

# PRODUTO
produto = st.text_input("📦 Qual produto vamos vender?")

# ESTILO
estilo = st.selectbox(
    "🎬 Escolha o estilo do vídeo:",
    ["TikTok Viral", "Review", "Oferta Rápida"]
)

# FOTO
foto = st.file_uploader(
    "📸 Envie a foto do produto",
    type=["png", "jpg", "jpeg"]
)

# FUNÇÃO VIDEO
def criar_video(imagem):

    img = Image.open(imagem).convert("RGB")

    # cria clip simples (SEM efeitos bugados)
    clip = ImageClip(img).set_duration(5)

    # formato vertical 9:16
    clip = clip.resize(height=1920)
    clip = clip.on_color(
        size=(1080,1920),
        color=(0,0,0),
        pos=("center","center")
    )

    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")

    clip.write_videofile(
        temp_video.name,
        fps=24,
        codec="libx264",
        audio=False
    )

    return temp_video.name


# BOTÃO
if st.button("🚀 Gerar Conteúdo PRO"):

    if foto:

        st.success("Imagem recebida!")

        video_path = criar_video(foto)

        st.video(video_path)

        with open(video_path, "rb") as file:
            st.download_button(
                "⬇️ Baixar Vídeo",
                file,
                file_name="lucky_video.mp4"
            )

    else:
        st.warning("Envie uma imagem primeiro.")
