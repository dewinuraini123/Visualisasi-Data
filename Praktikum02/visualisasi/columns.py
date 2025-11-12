import streamlit as st
from PIL import Image
import numpy as np
import time

st.title("Columns")
st.write("Kelompok: 19")
st.markdown("""
            1. Muhammad Daffa Shafwan - 0110222275
            2. Dewi Nuraini – 0110122122 
            3. Muhammad Saputra Adi Firmansyah – 0110222105  """)

#Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in column 1
col1.write("First Column")
col1.image("../assets/gambar1.jpg")
# Inserting Elements Elements in column 2
col2.write("Second Column")
col2.image("../assets/gambar1.jpg")

img = Image.open("../assets/gambar1.jpg")
st.title("Spaced-Out Columns")
# Defining no. of columns with size
cols = st.columns((3, 1, 2, 1))
cols[0].image(img)
cols[1].image(img)
cols[2].image(img)
cols[3].image(img)

img = Image.open("../assets/gambar1.jpg")
st.title("Padding")
# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)

img = Image.open("../assets/gambar1.jpg")
st.title("Grid")
# Defining no of Rows
for a in range(4):
# Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

st.title('Exapanders')
# Defining Expanders
with st.expander("Streamlit with Python"):
    st.write("Develop ML Applications in Minutes!!!!")

st.title("Container")
with st.container():
    st.write("Element Inside Container")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Elements Outside Container")

st.title("Out of Order Container")
# Defining Containers
container_one = st.container()
container_one.write("Elements One Inside Container")
st.write("Elements Outside Container")
# Now insert few more elements ini the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"{seconds} seconds have passed")
        time.sleep(1)
        st.write("Times up!")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a new user", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)

# home page
st.title("# Main page ")
st.write("This is Main Page")

# Second page
st.title("# Page 3 ")
st.write("You have navigated to page one")
