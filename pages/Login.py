from FrontEnd import *
from BackEnd import *

st.set_page_config(page_title="LogIn")

if __name__ == '__main__':
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox(label="Login"):
        customer(username, password)