# NOV 18

#NECESSARY IMPORTS
from XZNOM import *
from tkinter import Button
import tkinter as tk
import customtkinter

#THEMES
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#GEOMETRY
app = customtkinter.CTk()
app.title("XZNOM")
app.geometry("420x250")
app.minsize(420, 250)
app.maxsize(420, 250)

#LOGIN FUNCTION VARIABLES
LOGIN_ID = tk.StringVar()
LOGIN_PASS = tk.StringVar()
access = tk.StringVar()

#LOGIN FUNCTION
def LOGIN_FUNCTION():
    L = LOGIN(LOGIN_ID.get(),LOGIN_PASS.get(),access.get())
    if L.VALID_LOGIN() == True:
        if access.get() == "data":
            CLEAR()
            USER_DASHBOARD()
            print("Sucess")
        elif access.get() == "admin":
            CLEAR()
            ADMIN_DASHBOARD()
            print("Sucess")
    else:
        print("Unsucess")

#TRANSFER FUNCTION VARIABLES
RECEIVERS_ID = tk.StringVar()
AMT_TO_SENT = tk.StringVar()
CONFIRM_PASSWORD = tk.StringVar()

#TRANSFER FUNCTION 
def CONFIRM_FUNCTION():
    if LOGIN_PASS.get() == CONFIRM_PASSWORD.get():
        U = USER_CLASS(LOGIN_ID,LOGIN_PASS)
        U.TRANSFER_AMOUNT(RECEIVERS_ID,AMT_TO_SENT)
        
#WITHDRAW VARIABLES
AMT_TO_WITHDRAW = tk.StringVar()

#WITHDRAW FUNCTIONS VARIABLES
def WITHDRAW_FUNCTION():
    U = USER_CLASS(LOGIN_ID,LOGIN_PASS)
    U.WITHDRAW_AMOUNT(AMT_TO_WITHDRAW.get())

#LOADAMT VARIABLES
AMT_TO_LOAD = tk.StringVar()

#LOADAMT FUNCTION
def LOAD_FUNCTION():
    U = USER_CLASS(LOGIN_ID,LOGIN_PASS)
    U.LOAD_AMOUNT(AMT_TO_LOAD.get())

#CREATE NEW USER VARIABLE
NAME_ENTRY = tk.StringVar()
AGE_ENTRY = tk.StringVar()
LOCATION_ENTRY = tk.StringVar()
INCOME_ENTRY = tk.StringVar()
PWD_ENTRY = tk.StringVar()

#CREATE_NEW_USER_FUNCTION
def CREATE_NEW_USER_FUNCTION():
    TEMP_USER_GENERATED_ID = str(random.randint(123456789,987654321))
    DATA = {"ID":TEMP_USER_GENERATED_ID,"Name":NAME_ENTRY.get(),"AGE":AGE_ENTRY.get(),"LOCATION":LOCATION_ENTRY.get(),"INCOME":INCOME_ENTRY.get(),"PWD":PWD_ENTRY.get()}
    A = ADMIN_CLASS()
    A.CREATE_NEW_USER(TEMP_USER_GENERATED_ID,DATA)

#EDIT DATABASE VARIABLE
UPDATE_CATEGORY_ENTRY = tk.StringVar()
UPDATE_LATEST_VALUE_ENTRY = tk.StringVar()

#EDIT DATABASE FUNCTION
def EDIT_DATABASE_FUNCTION():
    A = ADMIN_CLASS()
    A.EDIT_DATA_BASE(UPDATE_CATEGORY_ENTRY.get(),UPDATE_LATEST_VALUE_ENTRY.get())

#DELETING USER DATA VARIABLE
DELETE_DATA_ENTRY = tk.StringVar()

#DELETING USER DATA FUNCTION
def DELETE_DATA_FROM_DATABASE():
    A = ADMIN_CLASS()
    A.DELETING_USER_DATA(DELETE_DATA_ENTRY.get())
    

#ESSENTIALS FUNCTIONS
def info():
    app.title("ABOUT US")
    ABOUTUSNOTE = customtkinter.CTkLabel(master=app, text="XENOM is designed to \nprovide the better \nE-WALLET MONETRY transfer \nwith better client support\n\n\n\n\nDeveloped by EXTERONOUS Head Team").grid(row=1, column=1, padx=90, pady=25)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=lambda:[CLEAR(), MAIN_LOGIN()]).grid(row=4, column=1, padx=30, pady=0)

#ESSENTIALS FUNCTIONS
def CLEAR():
    list = app.grid_slaves()
    for l in list:l.destroy()

#MAIN FUNCTIONS
def MAIN_LOGIN():
    app.title("XZNOM")
    USERLOGIN_BUTTON = customtkinter.CTkButton(master=app, text="User Login",command=lambda:[CLEAR(), ENTRY()]).grid(row=0, column=1, padx=130, pady=30)
    ABOUTUS_BUTTON = customtkinter.CTkButton(master=app, text="About Us",command=lambda:[CLEAR(), info()]).grid(row=1, column=1, padx=0, pady=0)
    QUIT_BUTTON = customtkinter.CTkButton(master=app, text="Quit", command=quit).grid(row=2, column=1, padx=130, pady=30)
    
def ENTRY():
    ACC_NUM_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="ID Number",textvariable=LOGIN_ID).grid(row=0, column=1, padx=130, pady=20)
    ACC_PASS_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="ID Password",textvariable=LOGIN_PASS).grid(row=1, column=1, padx=0, pady=0)
    ACC_ACCESS_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Account Acess Point",textvariable=access).grid(row=2, column=1, padx=130, pady=20)
    LOGIN_BUTTON = customtkinter.CTkButton(master=app, text="Login",command=LOGIN_FUNCTION).grid(row=3, column=1, padx=0, pady=0)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=lambda:[CLEAR(), MAIN_LOGIN()]).grid(row=4, column=1, padx=130, pady=20)
    
def USER_DASHBOARD():
    U = USER_CLASS(LOGIN_ID.get(),LOGIN_PASS.get())
    TEMP_DICT = U.SHOW_USERDATA()
    USER_DETAILS = customtkinter.CTkLabel(master=app, text=(TEMP_DICT["NAME"],TEMP_DICT["BALANCE"],TEMP_DICT["LOCATION"],TEMP_DICT["CONTACT"]))
    TRANSACTION_BUTTON = customtkinter.CTkButton(master=app, text="Transfer",command=lambda:[CLEAR(),TRANSFER()]).grid(row=3, column=1, padx=130, pady=30)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=lambda:[CLEAR(), MAIN_LOGIN()]).grid(row=4, column=1, padx=0, pady=0)

def TRANSFER():
    RECEIVERS_ACCOUNTNUM = customtkinter.CTkEntry(master=app,placeholder_text="Account Number",textvariable=RECEIVERS_ID).grid(row=0, column=1, padx=130, pady=15)
    AMOUNT_TO_SEND = customtkinter.CTkEntry(master=app,placeholder_text="Amount",textvariable=AMT_TO_SENT).grid(row=1, column=1, padx=0, pady=0)
    ACC_HOLDER_PASS = customtkinter.CTkEntry(master=app,placeholder_text="Password",textvariable=CONFIRM_PASSWORD).grid(row=2, column=1, padx=130, pady=30)
    SEND_BUTTON = customtkinter.CTkButton(master=app, text="Send",command=CONFIRM_FUNCTION).grid(row=3, column=1, padx=0, pady=0)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=lambda:[CLEAR(), USER_DASHBOARD()]).grid(row=4, column=1, padx=130, pady=30)

def WITHDRAW():
    AMT_TO_WITHDRAW = customtkinter.CTkEntry(master=app, placeholder_text="WithDraw Amount",textvariable=AMT_TO_WITHDRAW).grid(row=0,column=1,padx=130,pady=15)
    WITHDRAW_BUTTON = customtkinter.CTkButton(master=app, text="WithDraw Confirm", command=lambda:[CLEAR(),WITHDRAW_FUNCTION()]).grid(row=1,column=1,padx=130,pady=0)   
    
def LOAD_MONEY():
    AMT_TO_LOAD = customtkinter.CTkEntry(master=app, placeholder_text="Load Money", textvariable=AMT_TO_LOAD).grid(row=0,column=1,padx=130,pady=15)
    LOADAMT_BUTTON = customtkinter.CTkEntry(master=app, placeholder_text="LoadMoney Confirm", command=lambda:[CLEAR(),LOAD_FUNCTION()]).grid(row=1,column=1,padx=130,pady=0)
    
def ADMIN_DASHBOARD():
    SHOW_DATABASE_BUTTON = customtkinter.CTkButton(master=app, text="Show DataBase").grid(row=0, column=1, padx=130, pady=15)
    CREATE_NEW_USER_BUTTON = customtkinter.CTkButton(master=app, text="Create New User").grid(row=1, column=1, padx=0, pady=0)
    EDIT_DATABASE_BUTTON = customtkinter.CTkButton(master=app, text="Edit DataBase").grid(row=2, column=1, padx=130, pady=15)
    DELETE_BUTTON = customtkinter.CTkButton(master=app, text="Delete").grid(row=3, column=1, padx=0, pady=0)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=lambda:[CLEAR(), MAIN_LOGIN()]).grid(row=4, column=1, padx=130, pady=15)

def SHOW_DATABASE():
    A = ADMIN_CLASS()
    DATA_DICT = A.SHOW_DATA_BASE()
    USER_DETAILS = customtkinter.CTkLabel(master=app, text=(DATA_DICT))
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=CLEAR()).grid(row=4, column=1, padx=130, pady=15)

def CREATE_NEW_USER():
    NAME_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Name", textvariable=NAME_ENTRY).grid(row=0, column=1, padx=130, pady=30)
    AGE_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Age",textvariable=AGE_ENTRY).grid(row=1, column=1, padx=0, pady=0)
    LOCATION_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Location",textvariable=LOCATION_ENTRY).grid(row=2, column=1, padx=130, pady=30)
    INCOME_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Income",textvariable=INCOME_ENTRY).grid(row=3, column=1, padx=0, pady=0)
    PWD_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Password",textvariable=PWD_ENTRY).grid(row=4, column=1, padx=130, pady=30)
    CREATE_BUTTON = customtkinter.CTkButton(master=app, text="Create Account", command=lambda:[CLEAR(),CREATE_NEW_USER_FUNCTION()]).grid(row=5, column=1, padx=0, pady=0)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=CLEAR()).grid(row=6, column=1, padx=130, pady=15)

def EDIT_DATABASE():
    UPDATE_CATEGORY_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Category",textvariable=UPDATE_CATEGORY_ENTRY).grid(row=0, column=1, padx=130, pady=30)
    UPDATE_LATEST_VALUE_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Update Value With",textvariable=UPDATE_LATEST_VALUE_ENTRY).grid(row=1, column=1, padx=0, pady=0) 
    UPDATE_BUTTON = customtkinter.CTkButton(master=app, text="Update", command=lambda:[CLEAR(),EDIT_DATABASE_FUNCTION()]).grid(row=2, column=1, padx=130, pady=15)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=CLEAR()).grid(row=3, column=1, padx=0, pady=0)                                                                    

def DELETE_DATA_FROM_DATABASE():
    DELETE_DATA_ENTRY = customtkinter.CTkEntry(master=app,placeholder_text="Enter User ID TO Delete",textvariable=DELETE_DATA_ENTRY).grid(row=0, column=1, padx=130, pady=30)
    DELETE_BUTTON = customtkinter.CTkButton(master=app, text="Delete Data", command=lambda:[CLEAR(),DELETE_DATA_FROM_DATABASE()]).grid(row=2, column=1, padx=0, pady=0)
    BACK_BUTTON = customtkinter.CTkButton(master=app, text="Back", command=CLEAR()).grid(row=3, column=1, padx=130, pady=30)

MAIN_LOGIN()

app.mainloop()