import streamlit as st
import pandas as pd
from PIL import Image
from FrontEnd import *
from BackEnd import *

if __name__ == '__main__':
    st.set_page_config(
        page_title="CAR SALES MANAGEMENT SYSTEM",
        page_icon="icon.jpeg"
    )

    image = Image.open('image.jpg')

    st.image(image)

    for_key()
    cust_create_table()
    car_create_table()
    seller_create_table()
    order_create_table()
    inventory_create_table()
    create_trigger()

    st.write("# WELCOME TO THE CAR SALES MANAGEMENT SYSTEM")

    st.markdown(
        '''
        The car sales management system is an app framework built using streamlit and sqlite3, to place orders for cars online and to allow for a more efficient data maintainance system for administrators.
        
        '''
    )

    creators = {"NAME": ["S N SHREYAS", "TEJAS KODOOR"], "USN": ["1BG20CS129", "1BG20CS117"]}
    with st.expander("CREATED BY"):
        creators_df = pd.DataFrame(data=creators)
        st.dataframe(creators_df)