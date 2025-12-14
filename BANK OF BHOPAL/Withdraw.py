from dbConnect import mysql_connection
import mysql.connector
from Exceptions import InvalidFund,InvalidPinError,InsufficientFundError
from Validations import Validation
class Withdraw:
    def account_validation(self):
        try:
            self.acc_no = int(input("Enter your account number : "))
            self.c = Validation.accno_validation(self)
            if self.c == 0:
                print("This account number is not exist , please enter valid account number !")
            else:
                self.amount = float(input("Enter amount to Withdraw :"))
                if self.amount < 0:
                    raise InvalidFund
                else:
                    self.pin = int(input("Enter your account pin : "))
                    self.p = Validation.pin_validation(self)
                    if self.p == 0:
                        raise InvalidPinError
                    else:
                        self.current_bal = Validation.remaining_balance(self)
                        if self.current_bal >= self.amount:
                            self.AmountWithdraw()
                        else:
                            raise InsufficientFundError

        except ValueError:
            print("Don't enter alnum, str , and special symbols ")
        except InvalidFund:
            print("Please enter amount greater than 0")
        except InvalidPinError:
            print("Please enter valid account pin !")
        except InsufficientFundError:
            print("Your account have no sufficient amount !")

    def AmountWithdraw(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            qu = "update Customer_Info set bal = bal- %d where acc_no = %d" %(self.amount,self.acc_no)
            cur.execute(qu)
            conn.commit()
        except mysql.connector.DatabaseError:
            print("Please wait, there is a problem in database we shortly sort out this problem !")
        else:
            print("-"*100)
            print("Your amount {} withdraw succesfully" .format(self.amount))
            print("Thanks for using BANK OF BHOPAL !")
            print("-"*100)


