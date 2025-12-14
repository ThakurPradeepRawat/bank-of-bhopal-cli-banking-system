from dbConnect import mysql_connection
from Exceptions import InvalidPinError
from Validations import Validation
import mysql.connector
class CustomerInfo:
    def accInfo(self):
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
                    self.CustomerDetail()
        except ValueError:
            print("Don't enter alnum, str , and special symbols ")
        except InvalidPinError:
            print("Please enter valid account pin !")
    def CustomerDetail(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            qu = "select * from Customer_Info where acc_no=%d" % (self.acc_no)
            cur.execute(qu)
            print("-" * 100)
            for colinfo in cur.description:
                print("\t{}".format(colinfo[0]), end="\t")
            print()
            print("-" * 100)
            records = cur.fetchall()
            for record in records:
                for val in record:
                    print("\t{}".format(val), end="\t")
                print()
            print("-" * 100)
        except mysql.connector.DatabaseError as db:
            print(f"{db}Please wait, there is a problem in database we shortly sort out this problem !")






