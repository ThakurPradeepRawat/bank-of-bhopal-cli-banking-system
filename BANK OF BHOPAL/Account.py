import numpy as np
import mysql.connector
from dbConnect import mysql_connection
from Exceptions import SpaceError,EmptyError,InvalidNameError,InvalidFund
from Validations import Validation
class Account:
    def accountDetail(self):
        while(True):
            try:
                self.cname = Validation.namevalidation(input("Enter customer name : "))
                self.bal = Validation.balvalidation(float(input("Enter account opening amount : ")))
                self.pin = int(input("Enter account pin : "))
            except SpaceError:
                print("Please Don't enter spaces as customer name  --- try again !")
            except EmptyError:
                print("Please Don't make empty customer name   --- try again ")
            except InvalidNameError:
                print("Please enter valid customer name --- try again")
            except ValueError:
                print("Please Don't enter alnums , string and symbols as amount or pin ")
            except InvalidFund:
                print("Please enter account Opening amount more than 0")
            else:
                self.acc_no = np.random.randint(100000 , 100000000)
                break
    def create_account(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            qu = "insert into Customer_Info values(%d,'%s',%f,%d)" % (self.acc_no, self.cname, self.bal, self.pin)
            cur.execute(qu)
            conn.commit()
            print("*" * 100)
            print("Your account created successfully !")
            print("This is your account number : {}".format(self.acc_no))
            print("Thanks for opening account in BANK OF BHOPAL !")
            print("*" * 100)
        except mysql.connector.DatabaseError as db:
            print(f"{db}Please wait, there is a problem in database we shortly sort out this problem !")











