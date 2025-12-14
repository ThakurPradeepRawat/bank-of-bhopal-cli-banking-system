from Validations import Validation
from Exceptions import InvalidPinError
from dbConnect import mysql_connection
import mysql.connector
class Pin:
    def accInfo2(self):
        try:
            self.acc_no = int(input("Enter your account number : "))
            self.c = Validation.accno_validation(self)
            if self.c == 0:
                print("This account number is not exist , please enter valid account number !")
            else:
                self.pin = int(input("Enter your account pin : "))
                self.p = Validation.pin_validation(self)
                if self.p == 0:
                    raise InvalidPinError
                else:
                    self.updatepin()
        except ValueError:
            print("Don't enter alnum, str , and special symbols ")
        except InvalidPinError:
            print("Please enter valid account pin !")
    def updatepin(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            self.newpin = int(input("Enter new account pin :"))
            qu = "update Customer_Info set pin = %d where acc_no = %d" % (self.newpin, self.acc_no)
            cur.execute(qu)
            conn.commit()
        except mysql.connector.DatabaseError:
            print("Please wait, there is a problem in database we shortly sort out this problem !")
        except ValueError:
            print("Don,t enter alnum, str , and special symbols ")
        else:
            print("-" * 100)
            print("Your pin updated succesfully !")
            print("Thanks for using BANK OF BHOPAL!")
            print("-" * 100)