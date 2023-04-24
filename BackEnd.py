##SQL DATABASE CODE
import sqlite3
from datetime import *

con = sqlite3.connect("rental_data.db", check_same_thread=False)  # connection may be shared across multiple threads
c = con.cursor()

def for_key():
    c.execute("PRAGMA foreign_keys = ON")
    con.commit()

def cust_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Customers(
                    U_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    C_Name VARCHAR(50) NOT NULL UNIQUE,
                    C_Password VARCHAR(50) NOT NULL,
                    C_Email VARCHAR(50) NOT NULL UNIQUE, 
                    C_State VARCHAR(50) NOT NULL,
                    C_Phno VARCHAR(50) NOT NULL 
                    )''')
    print('Customer Table create Successfully')


def customer_add_data(Cname, Cpass, Cemail, Cstate, Cnumber):
    c.execute('''INSERT INTO Customers (C_Name,C_Password,C_Email, C_State, C_Phno) VALUES(?,?,?,?,?)''',
              (Cname, Cpass, Cemail, Cstate, Cnumber,))
    con.commit()


def customer_view_all_data():
    c.execute('SELECT * FROM Customers')
    customer_data = c.fetchall()
    return customer_data


def customer_update(Cemail, Uid, Cnum):
    c.execute(''' UPDATE Customers SET C_Email = ? WHERE U_id = ?''', (Cemail, Uid))
    c.execute(''' UPDATE Customers SET C_Phno = ? WHERE U_id = ?''', (Cnum, Uid))
    con.commit()
    print("Updating")


def customer_delete(Uid):
    c.execute(''' DELETE FROM Customers WHERE U_id = ?''', (Uid,))
    con.commit()


def car_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Cars(
                C_id INTEGER PRIMARY KEY NOT NULL,
                Car_Name VARCHAR(50) NOT NULL,
                C_Price INT NOT NULL)
                ''')
    print('Car Table created Successfully')


def car_add_data(Cid, CarName, Cprice):
    c.execute('''INSERT INTO Cars (C_id, Car_Name, C_Price) VALUES(?,?,?)''', (Cid, CarName, Cprice))
    con.commit()


def car_view_all_data():
    c.execute('SELECT * FROM Cars')
    car_data = c.fetchall()
    return car_data


def car_update(Cprice, Cid):
    c.execute(''' UPDATE Cars SET C_Price = ? WHERE C_id = ?''', (Cprice, Cid))
    con.commit()
    print("Updating")


def car_delete(Cid):
    c.execute('''DELETE FROM Cars WHERE C_id = ?''', (Cid,))
    con.commit()

def seller_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Sellers(
                S_id INTEGER PRIMARY KEY NOT NULL,
                S_Name VARCHAR(100) NOT NULL UNIQUE,
                S_State VARCHAR(50) NOT NULL,
                S_Phno VARCHAR(50) NOT NULL)
                ''')
    print('Seller Table created Successfully')

def seller_add_data(Sid, Sname, Sstate, Snumber):
    c.execute('''INSERT INTO Sellers (S_id, S_Name, S_State, S_Phno) VALUES(?,?,?,?)''',
              (Sid, Sname, Sstate, Snumber))
    con.commit()


def seller_view_all_data():
    c.execute('SELECT * FROM Sellers')
    seller_data = c.fetchall()
    return seller_data


def seller_update(Sid, Snum):
    c.execute(''' UPDATE Sellers SET S_Phno = ? WHERE S_id = ?''', (Snum, Sid,))
    con.commit()
    print("Updating")


def seller_delete(Sid):
    c.execute(''' DELETE FROM Sellers WHERE S_id = ?''', (Sid,))
    con.commit()


def inventory_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Inventory(
                IC_id INTEGER NOT NULL,
                IC_Name VARCHAR(50) NOT NULL,
                S_id INTEGER NOT NULL,
                quantity INT DEFAULT NULL,
                PRIMARY KEY(IC_id,S_id),
                CONSTRAINT fk01 FOREIGN KEY (IC_id) REFERENCES Cars(C_id) ON DELETE CASCADE,
                CONSTRAINT fk03 FOREIGN KEY (S_id) REFERENCES Sellers(S_id) ON DELETE CASCADE)
                ''')
    print('Inventory Table created Successfully')

def inventory_add_data(Cid, Cname, Sid, Qty):
    c.execute('''INSERT INTO Inventory(IC_id,IC_Name,S_id,quantity) VALUES(?,?,?,?)''', (Cid, Cname, Sid, Qty))
    con.commit()


def inventory_view_all_data():
    c.execute('SELECT * FROM Inventory')
    inventory_data = c.fetchall()
    return inventory_data


def inventory_update(Qty, Cid, Sid):
    c.execute('''UPDATE Inventory SET quantity = ? WHERE IC_id = ? AND S_id = ?''', (Qty, Cid, Sid))
    con.commit()
    print("Updating")


def inventory_delete(Cid, Sid):
    c.execute('''DELETE FROM Inventory WHERE IC_id = ? AND S_id = ?''', (Cid, Sid))
    con.commit()


def order_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Orders(
                O_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                U_id INTEGER NOT NULL,
                C_id INTEGER NOT NULL,
                S_id INTEGER NOT NULL,
                O_Datetime INT DEFAULT NULL,
                O_Qty INT NOT NULL,
                CONSTRAINT fk04 FOREIGN KEY (C_id) REFERENCES Cars(C_id) ON DELETE CASCADE,
                CONSTRAINT fk05 FOREIGN KEY (S_id) REFERENCES Sellers(S_id) ON DELETE CASCADE,
                CONSTRAINT fk06 FOREIGN KEY (U_id) REFERENCES Customers(U_id) ON DELETE CASCADE)
                ''')
    print('Orders Table created Successfully')
    # c.execute('''ALTER TABLE orders AUTOINCREMENT=1000''')


def order_add_data(Uid, Cid, Sid, Qty):
    c.execute('''INSERT INTO Orders(U_id,C_id,S_id,O_Datetime,O_Qty)VALUES(?,?,?,?,?)''', (Uid, Cid, Sid, date.today(), Qty))
    con.commit()


def order_view_data(Uid):
    c.execute('SELECT * FROM Orders WHERE U_id = ?', Uid)
    order_data = c.fetchall()
    return order_data


def order_view_all_data():
    c.execute('SELECT * FROM Orders')
    order_all_data = c.fetchall()
    return order_all_data


def order_delete(Oid):
    c.execute(''' DELETE FROM Orders WHERE O_id = ?''', (Oid,))
    con.commit()


def create_trigger():
    c.execute('''CREATE TRIGGER IF NOT EXISTS inventory_trigger AFTER INSERT ON Orders
                    FOR EACH ROW
                    BEGIN

                    UPDATE Inventory
                    SET quantity=quantity-(SELECT O_Qty
                                            FROM Orders
                                            ORDER BY O_id DESC
                                            LIMIT 1)
                    WHERE IC_id=(SELECT C_id
                                FROM Orders
                                ORDER BY O_id DESC
                                LIMIT 1);
                    END''')
