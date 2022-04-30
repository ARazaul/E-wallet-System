import csv
import random
import datetime
import sys

def main_front():
    def transaction():
        date_time=datetime.datetime.now()
        user_transaction_info=[]
        print("\nSEND MONEY")
        sender_account_number,sender_key_pass,receiver_account_number,transfering_amount= input("Sender Account Number:"),input("Sender Account Password:"),input("Beneficiary Account Number:"),int(input("Amount:"))
        with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
            lines = file.readlines()
            for line in lines:
                if sender_account_number in line and sender_key_pass in line:
                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
                        transaction_data = csv.reader(file)
                        header = next(transaction_data)
                        for transaction_info in transaction_data:user_transaction_info.append(transaction_info)
                    for i in range(len(user_transaction_info)):
                        if sender_account_number in user_transaction_info[i]:senders_total_amount = user_transaction_info[i][6]
                    for j in range(len(user_transaction_info)):
                        if receiver_account_number in user_transaction_info[j]:receiver_total_amount = user_transaction_info[j][6]
                    calculated_amount_sender = int(senders_total_amount)-int(transfering_amount)
                    calculated_amount_receiver = int(receiver_total_amount)+int(transfering_amount)
                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
                        read_file_sender=file.read()
                        if sender_account_number in read_file_sender:read_file_sender=read_file_sender.replace(str(senders_total_amount),str(calculated_amount_sender))
                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv","w") as file:file.write(read_file_sender)
                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
                        read_file_receiver=file.read()
                        if receiver_account_number in read_file_receiver:read_file_receiver=read_file_receiver.replace(str(receiver_total_amount),str(calculated_amount_receiver))
                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv","w") as file:file.write(read_file_receiver)
                    with open("Python Final Project-Anamol Dhakal/Q1/transaction_history.csv","w+") as file:transaction_data=file.write(str(calculated_amount_sender)+" Sent From "+ str(sender_account_number) +" To "+str(receiver_account_number)+"."+str(date_time))
                    print("\nMoney Sent Sucessfully")
                    print("\nWe Protect Your Privacy")
                    main_front()
            else:
                print("\nError! 632\n")
                transaction()
    def user_login(account_number,key_pass,lines):
        def transaction_history():
            try:
                with open("Python Final Project-Anamol Dhakal/Q1/transaction_history.csv") as file:
                    transaction_data_ = file.read()
                    print(transaction_data_,"\nRedirecting To User Login...\n")
                    account_number,key_pass= input("Account Number:"),input("Password:")
                    user_login(account_number,key_pass,open("Python Final Project-Anamol Dhakal/Q1/data_base.csv").readlines())
            except:
                print("Back To Login Again")
                account_number,key_pass= input("Account Number:"),input("Password:")
                user_login(account_number,key_pass,open("Python Final Project-Anamol Dhakal/Q1/data_base.csv").readlines())
        user_info=[]
        with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
            lines = file.readlines()
            for line in lines:
                if account_number in line and key_pass in line:
                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
                        extracted_data = csv.reader(file)
                        header = next(extracted_data)
                        for user_cred in extracted_data:user_info.append(user_cred)
                    for i in range(len(user_cred)):
                        if account_number in user_info[i][5]:
                            for j in range(len(user_cred)):
                                if key_pass in user_info[j][4]:
                                    print("\nLogin Sucessfully\n")
                                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
                                        extracted_data = csv.reader(file)
                                        header = next(extracted_data)
                                        for info in extracted_data:user_info.append(info)
                                    for i in range(len(user_info)):
                                        if account_number in user_info[i] and key_pass in user_info[i]:
                                            print("Account Number:",(user_info[i])[5],"\nAmount:",(user_info[i])[6] ,"\nEmail Address:",(user_info[i])[3],"\nPhone Number:",(user_info[i])[2],"\n")
                                            print("1. Transaction\n2. Transaction History\n3. Quit")
                                            m_user_input = input("Enter:")
                                            if m_user_input=="1":
                                                transaction()
                                            elif m_user_input=="2":
                                                try:transaction_history()
                                                except:
                                                    print("\nTransaction Error!")
                                                    account_number,key_pass= input("Account Number:"),input("Password:")
                                                    user_login(account_number,key_pass,open("Python Final Project-Anamol Dhakal/Q1/data_base.csv").readlines())
                                            elif m_user_input=="3":
                                                sys.exit("Thank You For Your Time")
            else:
                print("\nError! 872")
                main_front()
    def admin_login():
        def create_account():
            acc_number=random.randint(152749224,965489336)
            fname,lname,ph_number = input("First Name: "),input("Last Name: "),input("Phone Number: ")
            email,password,amount = input("E-Mail Address: "),input("Set Password: "),input("Opening Amount: ")
            user_data = ("\n"+str(fname)+","+str(lname)+","+str(ph_number)+","+str(email)+","+str(password)+","+str(acc_number)+","+str(amount))
            with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv","a+") as file:file.write(user_data)
            print("\n.....Redirecting To Login Page.....\n")
            input("Press Any Key To Continue.")
        def main_login():
            admin_info=[]
            admin_id,admin_pass = input("\nAdmin ID:"),input("Admin Pass:")
            with open("Python Final Project-Anamol Dhakal/Q1/admin_data.csv") as file:
                admin_data = csv.reader(file)
                header = next(admin_data)
                for admin_info_ in admin_data:admin_info.append(admin_info_)
            for i in range(len(admin_info)):
                if admin_id in admin_info[i] and admin_pass in admin_info[i]:create_account()
                elif admin_id not in admin_info[i] and admin_pass not in admin_info[i]:
                    print("\n..Redirecting.. Back To Login...\n")
                    account_number,key_pass= input("Account Number:"),input("Password:")
                    user_login(account_number,key_pass,open("Python Final Project-Anamol Dhakal/Q1/data_base.csv").readlines())
        print("\n1. Create Account\n2. View Entire Server Data\n3. Quit")
        user_input = input()
        if user_input == "1":main_login()
        elif user_input == "2":
            admin_info=[]
            admin_id,admin_pass = input("\nAdmin ID:"),input("Admin Pass:")
            with open("Python Final Project-Anamol Dhakal/Q1/admin_data.csv") as file:
                admin_data = csv.reader(file)
                header = next(admin_data)
                for admin_info_ in admin_data:admin_info.append(admin_info_)
            for i in range(len(admin_info)):
                if admin_id in admin_info[i] and admin_pass in admin_info[i]:
                    with open("Python Final Project-Anamol Dhakal/Q1/data_base.csv") as file:
                        view_data = csv.reader(file)
                        header = next(view_data)
                        for _info_ in view_data:print("\n",",".join(_info_),"\n")
                    admin_login() 
                elif admin_id not in admin_info[i] and admin_pass not in admin_info[i]:
                    print("\nError! 432")
                    main_login()
                else:
                    print("\nError! 215")
                    main_login()
        elif user_input == "3":sys.exit("Thank You For Your Time")
        else:
            print("\nFunctional Error!\n")
            admin_login()
    print("\n1. User Login\n2. Admin Login\n3. Quit")
    user_input = input("\nEnter:")
    if user_input == "1":
        account_number,key_pass= input("Account Number:"),input("Password:")
        user_login(account_number,key_pass,open("Python Final Project-Anamol Dhakal/Q1/data_base.csv").readlines())
    elif user_input == "2":admin_login()
    elif user_input == "3":exit("Thank You For Your Time")
    else:
        print("\nError! 744")
        main_front() 
main_front()