import streamlit as st
import pandas as pd
from BackEnd import *

def admin():

    st.title("Car-Sales Database Dashboard")
    menu = ["Cars", "Customers", "Orders", "Sellers"]
    choice = st.sidebar.selectbox("Menu", menu)

    ##Cars
    if choice == "Cars":
        menu = ["Add", "View", "Update", "Delete", "Update Inventory"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Add":
            st.subheader("Add cars")

            col1, col2 = st.columns(2)

            with col1:
                Car_id = st.text_area("Enter the car id")
                Car_name = st.text_area("Enter the car name")
                Car_price = st.text_area("Enter the car price")
            with col2:
                Car_seller = st.text_area("Enter car seller's ID")
                Car_qty = st.text_area("Enter the number of cars")

            c.execute('''SELECT IC_id, S_id FROM Inventory WHERE IC_id = ? AND S_id = ?''', (Car_id, Car_seller,))
            existing_car_seller = c.fetchall()

            c.execute('''SELECT C_id FROM Cars WHERE C_id = ?''', (Car_id,))
            existing_car_id = c.fetchall()

            c.execute('''SELECT S_id FROM Sellers WHERE S_id = ?''', (Car_seller,))
            existing_sellerIds = c.fetchall()

            if st.button("Add car"):
                if existing_car_seller:
                    st.error("Entered car-seller pair already exists")
                elif (not existing_car_id) and (existing_sellerIds):
                    car_add_data(Car_id, Car_name, Car_price)
                    inventory_add_data(Car_id, Car_name, Car_seller, Car_qty)
                    st.success("Successfully added data")
                elif not existing_sellerIds:
                    st.error("Entered seller doesn't exist")
                else:
                    inventory_add_data(Car_id, Car_name, Car_seller, Car_qty)
                    st.success("Successfully added data")

        if choice == "View":
            st.subheader("Car details")
            car_result = car_view_all_data()
            inventory_result = inventory_view_all_data()

            with st.expander("View all car data"):
                car_df = pd.DataFrame(car_result, columns=["ID", "NAME", "PRICE"])
                st.dataframe(car_df)
            with st.expander("View current inventory"):
                inventory_df = pd.DataFrame(inventory_result, columns=["CAR ID", "CAR NAME", "SELLER ID", "QUANTITY"])
                st.dataframe(inventory_df)

        if choice == "Update":
            st.subheader("Update car details")
            c_id = st.text_area("Car ID")
            c_price = st.text_area("Car price")

            c.execute('''SELECT C_id FROM Cars WHERE C_id = ?''', (c_id,))
            carIds = c.fetchall()

            if st.button(label="UPDATE"):
                if not carIds:
                    st.error("Entered car doesn't exist")
                else:
                    car_update(c_price, c_id)
                    st.success("Price Successfully Updated")

        if choice == "Delete":
            st.subheader("Delete cars")
            C_id = st.text_area("Car ID")
            
            c.execute('''SELECT C_id FROM Cars WHERE C_id = ?''', (C_id,))
            carIds2 = c.fetchall()

            if st.button(label="DELETE"):
                if not carIds2:
                    st.error("Entered car doesn't exist")
                else:
                    car_delete(C_id)
                    st.success("Car Successfully Deleted")

        if choice == "Update Inventory":
            st.subheader("Update Inventory details")
            cars_id = st.text_area("Car ID")
            Seller_id = st.text_area("Seller ID")
            qty = st.text_area("Car quantity")

            c.execute('''SELECT IC_id, S_id FROM Inventory WHERE IC_id = ? AND S_id = ?''', (cars_id, Seller_id,))
            existing_car_seller2 = c.fetchall()

            if st.button(label="UPDATE"):
                if existing_car_seller2:
                    inventory_update(qty, cars_id, Seller_id)
                    st.success("Inventory Successfully Updated")
                else:
                    st.error("Entered car-seller pair doesn't exist")


    ##CUSTOMERS
    elif choice == "Customers":
        menu = ["View", "Update", "Delete"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "View":
            st.subheader("Customer Details")
            cust_details = customer_view_all_data()
            with st.expander("View all customer data"):
                cust_df = pd.DataFrame(cust_details, columns=["ID", "NAME", "PASSWORD", "E-MAIL", "STATE", "PHONE NO."])
                st.dataframe(cust_df)

        if choice == "Update":
            st.subheader("Update Customer Details")
            cust_id = st.text_area("Customer ID")
            cust_email = st.text_area("E-mail")
            cust_ph = st.text_area("Phone number") 

            c.execute('''SELECT U_id FROM Customers WHERE U_id = ?''', (cust_id,))
            customerIds = c.fetchall()

            if st.button(label = "UPDATE"):
                if not customerIds:
                    st.error("Entered user doesn't exist")
                else:
                    customer_update(cust_email, cust_id, cust_ph)
                    st.success("User information updated successfully")

        if choice == "Delete":
            st.subheader("Delete customer")
            Cust_id = st.text_area("Customer ID")

            c.execute('''SELECT U_id FROM Customers WHERE U_id = ?''', (Cust_id,))
            customerIds2 = c.fetchall()

            if st.button(label="DELETE"):
                if not customerIds2:
                    st.error("Entered user doesn't exist")
                else:
                    customer_delete(Cust_id)
                    st.success("User information deleted successfully")


    ##ORDERS
    elif choice == "Orders":
        menu = ["View"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "View":
            st.subheader("Order Details")
            order_details = order_view_all_data()
            with st.expander("View all order data"):
                order_details_df = pd.DataFrame(order_details, columns=["ORDER ID", "CUSTOMER ID", "CAR ID", "SELLER ID", "ORDER DATE", "ORDER QUANTITY"])
                st.dataframe(order_details_df)


    ##SELLERS
    elif choice == "Sellers":
        menu = ["Add", "View", "Update", "Delete"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Add":
            st.subheader("Add seller")

            col3, col4 = st.columns(2)

            with col3:
                seller_id = st.text_area("Enter seller ID")
                seller_name = st.text_area("Enter seller name")
            with col4:
                seller_state = st.text_area("Enter seller's state")
                seller_number = st.text_area("Enter seller's phone number")

            c.execute('''SELECT S_id FROM Sellers WHERE S_id = ?''', (seller_id,))
            sellerIds = c.fetchall()

            if st.button("Add seller"):
                if not sellerIds:
                    seller_add_data(seller_id, seller_name, seller_state, seller_number)
                    st.success("Successfully added seller")
                else:
                    st.error("Entered seller already exists")

        if choice == "View":
            st.subheader("Seller details")
            seller_details = seller_view_all_data()
            with st.expander("View all seller details"):
                seller_details_df = pd.DataFrame(seller_details, columns=["ID", "NAME", "STATE", "PHONE NO."])
                st.dataframe(seller_details_df)

        if choice == "Update":
            st.subheader("Update seller details")
            s_id = st.text_area("Seller ID")
            s_num = st.text_area("Seller's phone number")

            c.execute('''SELECT S_id FROM Sellers WHERE S_id = ?''', (s_id,))
            sellerIds2 = c.fetchall()

            if st.button(label="UPDATE"):
                if not sellerIds2:
                    st.error("Entered seller doesn't exist")
                else:
                    seller_update(s_id, s_num)
                    st.success("Seller details updated successfully")

        if choice == "Delete":
            st.subheader("Delete sellers")
            S_id = st.text_area("Seller ID")

            c.execute('''SELECT S_id FROM Sellers WHERE S_id = ?''', (S_id,))
            sellerIds3 = c.fetchall()

            if st.button(label="DELETE"):
                if not sellerIds3:
                    st.error("Entered seller doesn't exist")
                else:
                    seller_delete(S_id)
                    st.success("Seller deleted successfully")



def getAuthenticate(userName, passWord):
    c.execute("SELECT C_Password FROM Customers WHERE C_Name = ?", (userName,))
    cust_password = c.fetchall()

    if cust_password[0][0] == passWord:
        return True
    else:
        return False

def invalidUser(userName, passWord):
    c.execute("SELECT C_Password FROM Customers WHERE C_Name = ?", (userName,))
    Cust_password = c.fetchall()

    if len(Cust_password) == 0:
        return True
    else:
        return False


def customer(username, password):
    if invalidUser(username, password):
        st.error("Account does not exist")
    else:
        if getAuthenticate(username, password):
            print("In customer")
            st.title("Welcome To The Car Showroom")

            menu = ["Place order", "View orders"]
            choice = st.sidebar.selectbox("Menu", menu)

            if choice == "Place order":
                st.subheader("Place order")

                inventory_result = inventory_view_all_data()
                with st.expander("View current inventory"):
                    inventory_df = pd.DataFrame(inventory_result, columns=["CAR ID", "CAR NAME", "SELLER ID", "QUANTITY"])
                    st.dataframe(inventory_df)

                c.execute("SELECT U_id FROM Customers WHERE C_Name=?", (username,))
                U_id = c.fetchall()
                Uid = U_id[0][0]
                Cid = st.text_area("Enter car ID")
                Sid = st.text_area("Enter seller ID")
                Qty = st.text_area("Enter number of cars")

                c.execute('''SELECT quantity FROM Inventory WHERE IC_id = ?''', (Cid,))
                car_quantity = c.fetchall()

                c.execute('''SELECT IC_id, S_id FROM Inventory WHERE IC_id = ? AND S_id = ?''', (Cid, Sid,))
                existing_car_seller2 = c.fetchall()

                c.execute('''SELECT C_id FROM Cars WHERE C_id = ?''', (Cid,))
                existing_car_id2 = c.fetchall()

                c.execute('''SELECT S_id FROM Sellers WHERE S_id = ?''', (Sid,))
                existing_sellerIds2 = c.fetchall()

                

                if st.button("Place order"):
                    if not existing_car_id2:
                        st.warning("Entered car doesn't exist")
                    
                    if not existing_sellerIds2:
                        st.warning("Entered seller doesn't exist")
                    
                    if not existing_car_seller2:
                        st.warning("Enterd seller doesn't sell this car")

                    elif not car_quantity:
                        st.error("Specified car not available")
                    elif (car_quantity[0][0] < int(Qty)):
                        st.warning("Specified number of cars unavailable")
                    else:
                        order_add_data(Uid, Cid, Sid, Qty)
                        st.success("Successfully placed order")

            if choice == "View orders":
                st.subheader("Your Order Details")

                c.execute("SELECT O.* FROM Orders O, Customers C WHERE O.U_id=C.U_id AND C.C_Name = ?", (username,))
                cust_orders = c.fetchall()
                with st.expander("View all order details"):
                    cust_orders_df = pd.DataFrame(cust_orders, columns=["ORDER ID", "CUSTOMER ID", "CAR ID", "SELLER ID", "SALE DATE", "SALE QUANTITY"])
                    st.dataframe(cust_orders_df)

        else:
            st.warning("Wrong username or password")
