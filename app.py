import streamlit as st

st.title("🤖 Lucky IA")

produto = st.text_input("🛍️ Qual produto vamos vender?")

if st.button("Criar roteiro"):
    roteiro = f"""
    Eu não esperava gostar tanto desse {produto}.
    Sério, virou meu favorito do dia a dia.
    Se você gosta de praticidade, vale muito a pena.
    O link está na sacolinha antes que acabe.
    """

    st.write("🎬 Roteiro criado:")
    st.write(roteiro)
