import streamlit as st

st.title("🤖 Lucky IA")

produto = st.text_input("🛍️ Qual produto vamos vender?")

if st.button("Criar roteiro"):
    roteiro = import random

roteiros = [
    f"Testei o {produto} e não achei que ia gostar tanto. Facilita MUITO o dia a dia!",
    f"Se você ainda não conhece esse {produto}, você está perdendo tempo.",
    f"Comprei o {produto} sem expectativa nenhuma… e virou meu favorito.",
    f"Esse {produto} está viralizando e agora eu entendi o motivo.",
    f"O {produto} resolveu um problema que eu tinha há anos."
]

if st.button("Criar roteiro"):
    st.write(random.choice(roteiros))

    st.write("🎬 Roteiro criado:")
    st.write(roteiro)
