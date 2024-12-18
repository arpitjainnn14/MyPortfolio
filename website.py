import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

file_read=pd.read_csv("C:/Users/ARPIT JAIN/Project-2/data.csv",sep=";")

col1, col2 = st.columns(2)

with col1:
    st.image("C:/Users/ARPIT JAIN/Project-2/images/my.jpg")
with col2:
    st.title("Arpit Jain")
    st.info("Currently a third-year student at VIT Bhopal, with a keen interest in AI and Python.")

st.text("Below you can find many of the projects i have worked on, feel free to connect with me!")

#this creates a colums for the lower part of the website
col3,col4=st.columns(2)

# this allows the title should be on the left side of the page
with col3:
    #[:10] allows the first 10 title to be on the left side.
    for index,row in file_read[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("C:/Users/ARPIT JAIN/Project-2/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

#this allows the title should be on the right side of the page
with col4:
    #[10:] allows the last 10 title to be on the right side.
    for index,row in file_read[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("C:/Users/ARPIT JAIN/Project-2/images/"+ row["image"])
        st.write(f"[Source Code]({row['url']})")