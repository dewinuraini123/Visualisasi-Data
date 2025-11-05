import streamlit as st
import time
st.title('Creating a Button')
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the button')
else:
    st.write('You have not clicked the button')


st.title('Creating Radio Button')
# Defining Radio Button
gender = st.radio(
"Select Your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female")
else:
    st.write("You have selected Others.")


st.title('Creating Checkboxes')
st.write('Select your Hobies:')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')


st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))


st.title('Multi-Select')
# Defining Multi_select with Pre-Selection
hobbies = st.multiselect(
'What are your Gobbies',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Srawing', 'Hiking'],
['Reading', 'Playing'])


st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
label="Download Image",
data=open("austria.jpg", "rb"),
file_name="austria.jpg",
mime="image/jpg"
)


st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')


st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientist')