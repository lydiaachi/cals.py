import streamlit as st 
from PIL import Image 
 

st.title("calculator")
img = Image.open("pix.jpg")
st.sidebar.image

col1, col2, col3 = st.columns(3)

def add (a,b):
    a = a + b
    return a

def subtract(a,b):
    b = a - b
    return b

def multiple (a,b):
    c = a * b
    return c


x = st.number_input("input your first number")
y = st.number_input("input your next number")


with col1:
  if st.button("add"):
     st.write(add(x,y))

with col2:
   if st.button("subtract"):
      st.write(subtract(x,y))

with col3:
   if st.button("Multiple"):
      st.write(multiple(x,y))


