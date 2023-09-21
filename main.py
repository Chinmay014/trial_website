import streamlit as st


st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/profile2.jpg")

with col2:
    st.title("Chinmay Sharma")
    content = """Hello there and welcome to my website! My name is Chinmay, a masters student graduate from Chalmers University, Sweden. I like to program and automate tasks. I also like talking about video games and Cars."""
    st.info(content)