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
    st.write(tags)
