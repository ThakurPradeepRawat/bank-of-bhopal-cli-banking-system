from dbConnect import mysql_connection
from Exceptions import InvalidFund
from Validations import Validation
import mysql.connector
class Deposit:
    def account_info(self):
        try:
            self.acc_no = int(input("Enter your account number : "))
            self.c = Validation.accno_validation(self)
            if self.c == 0:
                print("This account number is not exist , please enter valid account number !")
            else:
                self.amount = float(input("Enter amount to deposit :"))
                if self.amount < 0:
                    raise InvalidFund
                else:
                    self.AmountDeposit()
        except ValueError:
            print("Don,t enter alnum, str , and special symbols ")
        except InvalidFund:
            print("Please Enter Deposit amount greater than 0 ")
    def AmountDeposit(self):
        try:
            conn =mysql_connection()
            cur = conn.cursor()
            qu = "update Customer_Info set bal = bal+ %d where acc_no = %d" %(self.amount,self.acc_no)
            cur.execute(qu)
            conn.commit()
        except mysql.connector.DatabaseError:
            print("Please wait, there is a problem in database we shortly short out this problem !")
        else:
            print("-"*100)
            print("Your amount {} Deposited succesfully" .format(self.amount))
            print("Thanks for using BANK OF BHOPAL !")
            print("-"*100)





