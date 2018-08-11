#!/usr/bin/python
# -*- coding: utf-8 -*-




def update(last):
    file = open("database.csv","r")
    fileop= open("new.csv","w")
    updated= last.split(",")
    fileop.write(file.readline())
    new = file.readline()
    while new != '':
        store = new.split(",")
        if store[0]==updated[0]:
            fileop.write(last)
            new = file.readline()
        else:
            fileop.write(new)
            store.clear()
            new = file.readline()
    file.close()
    fileop.close()
    fileop = open("database.csv","w")
    fileip= open("new.csv","r")
    #new=fileip.readline()
    #while new != '':
     #   fileop.write(new)
      #  new=fileip.readline()
    new = fileip.read()
    fileop.write(new)
    fileip.close()
    fileop.close()
    


def withdrawl(data):
    amount=int(input("Enter the amount to Withdrawl:"))
    if amount>0 and amount<20000 and amount%100==0:
        if int(data[2])>amount:
            data[2]=int(data[2])-amount
            print("Amount Withdrawl\nTotal Amount={}".format(data[2]))
            string = str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n"
            update(string)
            return 1
        else:
            print("Not Enough Balance")
            return 0
    else:
        print("enter amount in the range 0 to 20000 in multiples of 100 only")



def deposit(data):
    amount=int(input("Enter the amount to Deposit:"))
    if amount>0 and amount<20000 and amount%100==0:
        data[2]=int(data[2])+amount
        print("Amount Deposited\nTotal Amount={}".format(data[2]))
        string = str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n"
        update(string)
    else:
        print("enter amount in the range 0 to 20000 in multiples of 100 only")



def credit(data,amount):
    data[2]=int(data[2])+amount
    string = str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n"
    update(string)





def debit(data,amount):
    if int(data[2])>amount:
        data[2]=int(data[2])-amount
        print("Amount Transferred\nTotal Amount={}".format(data[2]))
        string = str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n"
        update(string)
        return 1
    else:
        print("Not Enough Balance")
        return 0
    
    

def transfer(data):
    file = open("database.csv","r")
    phone=input("Enter the Phone number to send money:")
    phone=(phone+"\n")
    amount=int(input("Enter Amount"))
    flag=0
    new=file.readline()
    while new != '':
        store = new.split(",")
        if store[-1]==phone:
            flag=1
            if debit(data,amount):
                credit(store,amount)
            else:
                print("Unable to Transfer")
        new=file.readline()
                
    if(flag==0):
        print("Phone not exist in database")
    file.close()
        
    
    






def transaction(data):
    print("Your Account Balance is:{}".format(data[2]))
    logout=1
    while(logout):
        choice=int(input("Enter Your choice\n0.Show Data\n1.Deposit\n2.Withdrawl\n3.Change Phone number\n4.Change Email Address\n5.Change Password\n6.MONEY TRANSFER\n7.Logout\n:"))
        if(choice==0):
            print("Amount={}\nPassword={}\nEmail={}\nPhone number={}\n".format(data[2],data[1],data[3],data[4]))
        elif(choice==1):
            deposit(data)
        elif(choice==2):
            withdrawl(data)
        elif(choice==3):
            phone=int(input("Enter the Phone Number:"))
            data[4]=phone
            string = str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n"
            update(string)
        elif(choice==4):
            email=input("Enter the Email Address:")
            data[3]=email
            string = str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n"
            update(string)
        elif(choice==5):
            password=input("Enter the New Password:")
            data[1]=password
            string = str(data[0])+","+str(data[1])+","+str(data[2])+","+str(data[3])+","+str(data[4])+"\n"
            update(string)
        elif(choice==6):
            transfer(data)
        elif(choice==7):
            logout=0
            print("logout Suceessfully")
        else:
            print("Invalid Choice")
            




def genotp(data):
    import smtplib
    import random
    gen=random.randint(1000,9999)
    receiverAddress=str(data[3])
    email="timcook732@gmail.com"
    Subject="OTP for Login"
    Message=("The One Time Password For login is:{}".format(gen))
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(email,"237koocmit")
    connection.sendmail(email,receiverAddress,("Subject: " +str(Subject) + "\n\n" +str(Message)))
    connection.quit()
    return gen
    





def startprog(data):
    gen=genotp(data)
    i=3
    while(i>0):
        otp=int(input("Enter the otp sent to your email:"))
        if otp==gen:
            print("Login Successful")
            transaction(data)
            break
        else:
            print("Invalid otp")
        i=i-1
    







#initial
if __name__=="__main__":
    choice='y'
    flag=0
    while choice =='Y' or choice=='y':
        login=input("enter the login id:")
        password=input("enter the password:")
        file_ip = open("database.csv","r")
        #variable new contains every new line scanned fron the file
        new = file_ip.readline()
        new = file_ip.readline()
        while new != '':
                    data = new.split(",")
                    if data[0]==login and data[1]==password:
                        flag=1
                        break
                    else:
                        data.clear()
                    new = file_ip.readline()
        file_ip.close()
        if flag==1:
            print("Login details matched")
            startprog(data)
            #print(data)
            choice=0
            choice=input("Type 'Y' for reLogin:")
        else:
            choice=input("Invalid input!!try again?  type 'Y' for reenter:")

            
