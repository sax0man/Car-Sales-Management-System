from FrontEnd import *
from BackEnd import *

st.set_page_config(page_title="Dashboard")


if __name__ == '__main__':
    for_key()
    cust_create_table()
    car_create_table()
    seller_create_table()
    order_create_table()
    inventory_create_table()
    create_trigger()

    menu = ["Login", "SignUp", "Admin"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox(label="Login"):
            customer(username, password)

    elif choice == "SignUp":
        st.subheader("Create New Account")

        cust_name = st.text_input("Name")
        cust_password = st.text_input("Password", type='password', key=1000)
        cust_password1 = st.text_input("Confirm Password", type='password', key=1001)
        col1, col2, col3 = st.columns(3)

        with col1:
            cust_email = st.text_area("Email ID")
        with col2:
            cust_state = st.text_area("State")
        with col3:
            cust_number = st.text_area("Phone Number")

        c.execute('''SELECT C_Name FROM Customers WHERE C_Name = ?''', (cust_name,))
        existing_username = c.fetchall()

        c.execute('''SELECT C_Email FROM Customers WHERE C_Email = ?''', (cust_email,))
        existing_emails = c.fetchall()

        if existing_username:
            st.warning("Username already taken, select different user name")
        if existing_emails:
            st.warning("Entered email used with an exixting acount, please enter different email")

        if st.button("Signup") and (not existing_username) and (not existing_emails):
            if cust_password == cust_password1:
                customer_add_data(cust_name,cust_password,cust_email, cust_state, cust_number,)
                st.success("Account Created!")
                st.info("Go to Login Menu to login")
            else:
                st.warning('Passwords dont match')

    elif choice == "Admin":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        # if st.sidebar.button("Login"):
        if st.sidebar.checkbox(label="Login"):
            if username == 'admin' and password == 'admin':
                admin()

