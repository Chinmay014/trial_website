import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/profile2.jpg")

with col2:
    st.title("Chinmay Sharma")
    content = """Hello there and welcome to my website! My name is Chinmay, a masters student graduate from Chalmers University, Sweden. I like to program and automate tasks. I also like talking about video games and Cars."""
    st.info(content)
content2 = """Below are some of the apps I have built. Feel free to contact me!"""
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv",sep=",")

with col3:
    for index,row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")