import json
import random
import string 
import os
from pathlib import Path
class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data=json.loads(fs.read())
            
    except Exception as err:
        print(" an exception Occured as {err}")
    
    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            json.dump(Bank.data,fs)
    @classmethod
    def __accountgenrate(cls):
            alpha=random.choices(string.ascii_letters,k=3)
            num=random.choices(string.digits,k=3)
            spchar=random.choices("!@#$%^&*",k=1)
            id=alpha+num+spchar
            random.shuffle(id)
            return"".join(id)   
    def createaccount(self):
        data={
            "name":input("enter your name:-"),
            "age":int(input("enter you age:-")),
            "pin":int(input("enter your pin:-")),
            "e-mail":input("enter your email:"),
            "accountno":Bank.__accountgenrate(),
            "balance":0
        }
        if(data['age'] < 18 or len(str(data['pin'])) != 4):
            print("You are not eligible for account")
        else:
            print("account has been created succesfully")
            for i in data:
                print(f"{i}:{data[i]}")
            print("note down your account number")
            Bank.data.append(data) 
            Bank.__update()  
    def deposit(self):
        accountnumber = input("Enter your account number: ")
        pin = int(input("Please enter your pin: "))

        userdata = [i for i in Bank.data if i["accountno"] == accountnumber and i['pin'] == pin]

        if len(userdata) == 0:
            print("Sorry, no data found")

        else:
            amount = int(input("How much do you want to deposit: "))
            for user in userdata:
                user["balance"] += amount

            Bank.__update()

            print("Amount deposited successfully")
    def withdrawmoney(self):
        accountnumber = input("Enter your account number: ")
        pin = int(input("Please enter your pin: "))

        userdata = [i for i in Bank.data if i["accountno"] == accountnumber and i['pin'] == pin]

        if len(userdata) == 0:
            print("Sorry, no data found")
        else:
            amount=int(input("enter amount to withdrawl="))
            for user in userdata:
                if user["balance"]<amount:
                    print("you can not withdrawl money")
                else:
                    user["balance"]-=amount
                    Bank.__update()
                    print("Amount withdrawl succesfully")
                    
    def detail(self):
        name=input("enter your name:-")
        accountno=input("enter your account no:-")
        userdata = [i for i in Bank.data if i["name"] == name and i["accountno"] ==accountno]
    
        if len(userdata) == 0:
            print("Sorry, no data found")
        else:
            for user in userdata:
                print("\nAccount Details")
                print("Name:", user["name"])
                print("Age:", user["age"])
                print("PIN:", user["pin"])
                print("Account Number:", user["accountno"])
                print("Balance:", user["balance"])
    
    def updatedetail(self):
        name=input("enter your name:-")
        accountno = input("Enter your account number:-")
        userdata = [i for i in Bank.data if i["name"] == name and i["accountno"] ==accountno]
    
        if len(userdata) == 0:
            print("Sorry, no data found")
        else:
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. PIN")
            print("3. Email")
            choice =int(input("enter your choice="))
            if(choice==1):
                name=input("enter your new name:-")
                userdata[0]["name"]=name
            elif(choice==2):
                pin=int(input("enter your new pin:-"))
                if(len(str(pin))==4):
                    userdata[0]["pin"]=pin
                else:
                    print("inavalid pin")
            elif(choice==3):
                email=input("enter your email:-")
                userdata[0]["email"]=email
            Bank.__update()
            print("Detail updated successfully")
            
    def deleteacc(self):
        pin=int(input("enter your pin:-"))
        accountno = input("Enter your account number:-")
        file=open(r"data.json", "r")
        data = json.load(file)

        found = False

        for i in data:
            if i["accountno"] == accountno and i["pin"] == pin:
                data.remove(i)
                found = True
                break

        if found:

            # update json file
            file =open(r"data.json", "w")
            json.dump(data, file, indent=4)

            print("Account deleted successfully")

        else:
            print("No account found")
        
            
print("Press 1 forecasting an account")
print("press 2 for Depositing the money")
print("press 3 for Withdrawal the money")
print("press 4 for detail")
print("press 5 for updating the detail")
print("press 6 for deleting your account")


choice=int(input("tell your choice="))
bk=Bank();
if choice==1:
    bk.createaccount()
if choice==2:
    bk.deposit()
if choice==3:
    bk.withdrawmoney()
if choice==4:
    bk.detail()    
if choice==5:
    bk.updatedetail()
if choice==6:
    bk.deleteacc()
