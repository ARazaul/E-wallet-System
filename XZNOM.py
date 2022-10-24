
#Importing some dependencies 
import csv, random, datetime, sys

#Importing FireBase dependencies
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#FIREBASE Section
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#Creating Admin Class
class ADMIN_CLASS():
    def __init__(self):
        WHOLE_DATA_EXTRACTION = db.collection('data').get()
        for DATA_EXTRACTION in WHOLE_DATA_EXTRACTION:
            DATA_DICT = {DATA_EXTRACTION.to_dict()}
            self.__DATA_DICT = DATA_DICT

    def SHOW_DATA_BASE(self):
        return self.__DATA_DICT
    
    def CREATE_NEW_USER(self,TEMP_USER_GENERATED_ID,DATA):
        db.collection('data').documents(TEMP_USER_GENERATED_ID).set(DATA)
    
    def EDIT_DATA_BASE(self,UPDATE_CATEGORY,UPDATE_LATEST_VALUE_FOR_USR):
        self.__UPDATED_LATEST_VALUE_FOR_USR = UPDATE_LATEST_VALUE_FOR_USR
        self.__UPDATE_CATEGORY = UPDATE_CATEGORY
        db.collection('data').document(self.__TEMP_USER_ID).update({self.__UPDATE_CATEGORY:self.__UPDATED_LATEST_VALUE_FOR_USR})
    
    def DELETING_USER_DATA(self,TEMP_USER_ID):
        self.__TEMP_USER_ID = input()
        db.collection('data').document(self.__TEMP_USER_ID).delete()

#Creating User Class
class USER_CLASS():
    def __init__(self,USER_ID,USER_PASSWORD):
        self.__USER_ID = USER_ID
        self.__USER_PASSWORD = USER_PASSWORD
        self.__UPDATED_LATEST_VALUE_FOR_USR = None
        self.__UPDATED_LATEST_VALUE_FOR_REC = None
        self.__USER_DATA_EXTRACTION = db.collection('data').documents(self.__USER_ID).get()
    
    def SHOW_USERDATA(self):
        return self.__USER_DATA_EXTRACTION
    
    def LOAD_AMOUNT(self,USER_INPUT_AMOUNT):
        self.__USER_INPUT_AMOUNT = USER_INPUT_AMOUNT
        self.__UPDATED_LATEST_VALUE_FOR_USR = ((self.__USER_DATA_EXTRACTION.to_dict())["BALANCE"]) + self.__USER_INPUT_AMOUNT
        db.collection('data').document(self.__USER_ID).update({"BALANCE":self.__UPDTED_LATEST_VALUE_FOR_USR})
    
    def WITHDRAW_AMOUNT(self,USER_INPUT_AMOUNT):
        self.__USER_INPUT_AMOUNT = USER_INPUT_AMOUNT
        self.__UPDATED_LATEST_VALUE_FOR_USR = ((self.__USER_DATA_EXTRACTION.to_dict())["BALANCE"]) - self.__USER_INPUT_AMOUNT
        db.collection('data').document(self.__USER_ID).update({"BALANCE":self.__UPDTED_LATEST_VALUE_FOR_USR})
    
    def TRANSFER_AMOUNT(self,RECV_USER_ID,USER_INPUT_AMOUNT):
        self.__UPDATD_LATEST_VALUE_FOR_REC = None
        self.__UPDATED_LATEST_VALUE_FOR_USR = None
        self.__RECV_USER_ID = RECV_USER_ID
        self.__USER_INPUT_AMOUNT = USER_INPUT_AMOUNT
        self.__RECV_USER_DATAEXTRACTION = db.collection('data').documents(self.__Rec_USER_ID).get()
        self.__UPDATED_LATEST_VALUE_FOR_REC = ((self.__RECV_USER_DATAEXTRACTION.to_dict())["BALANCE"]) + self.__USER_INPUT_AMOUNT
        self.__UPDATED_LATEST_VALUE_FOR_USR = ((self.__USER_DATA_EXTRACTION.to_dict())["BALANCE"]) - self.__USER_INPUT_AMOUNT
        db.collection('data').document(self.__RECV_USER_ID).update({"BALANCE":self.__UPDTED_LATEST_VALUE_FOR_REC})
        db.collection('data').document(self.__USER_ID).update({"BALANCE":self.__UPDTED_LATEST_VALUE_FOR_USR})

#Creating Show History 
class Show_History:
    def __init__(self):
        pass

#Creating LOGIN Class
class LOGIN():
    def __init__(self,Login_ID,Login_PASS,ACCESS):
        self.__Login_ID = Login_ID
        self.__Login_PASS = Login_PASS
        self.__ACCESS = ACCESS
        
    def VALID_LOGIN(self):
        try:
            DATA_EXTRACTION = db.collection(self.__ACCESS).document(self.__Login_ID).get()
            if self.__Login_PASS == (((DATA_EXTRACTION.to_dict()))["PASSWORD"]):
                print("Logged In Sucessful")
                return True
            else:
                print("LOGIN Unsucessful")
                return False
        except Exception as E:
            print("Error: ",E)