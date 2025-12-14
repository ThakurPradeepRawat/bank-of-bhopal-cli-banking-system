import mysql.connector
from dbConnect import mysql_connection
from Exceptions import SpaceError,EmptyError,InvalidNameError,InvalidFund
class Validation:
    @staticmethod
    def namevalidation(user):
        if user.isspace():
            raise SpaceError
        elif len(user) == 0:
            raise EmptyError
        else:
            User_name = user.split()
            valid = True
            for nam in User_name:
                if not (nam.isalpha()):
                    valid = False
                    break
            if valid == True:
                return user
            else:
                raise InvalidNameError
    @staticmethod
    def balvalidation(bal):
        if bal <=0:
            raise InvalidFund
        else:
            return bal

    @staticmethod
    def accno_validation(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            qu = "select acc_no from Customer_Info"
            cur.execute(qu)
            records = cur.fetchall()
            if (self.acc_no,) in records:
                return 1
            else:
                return 0
        except mysql.connector.DatabaseError as db :
            print("Please wait, there is a problem in database we shortly sort out this problem !")

    @staticmethod
    def  pin_validation(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            qu = "select pin from Customer_Info where acc_no=%d" % (self.acc_no)
            cur.execute(qu)
            records = cur.fetchall()
            for record in records:
                if (self.pin,) in records:
                    return 1
                else:
                    return 0
        except mysql.connector.DatabaseError as db:
            print("Please wait, there is a problem in database we shortly sort out this problem !")

    @staticmethod
    def remaining_balance(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            qu = "select bal from Customer_Info where acc_no=%d" % (self.acc_no)
            cur.execute(qu)
            records = cur.fetchall()
            for record in records:
                return record[0]
        except mysql.connector.DatabaseError as db:
            print("Please wait, there is a problem in database we shortly sort out this problem !")
            







