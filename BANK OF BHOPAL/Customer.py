from dbConnect import mysql_connection
import mysql.connector
class Bank:
    Bank_employee_id = 1195
    def checkemployee(self):
        try:
            self.id = int(input("Enter your Bank employee id : "))
            if self.id == Bank.Bank_employee_id:
                self.AllCustomer()
            else:
                print("This is not bank employee id , please enter valid employee id !")
        except ValueError:
            print("Please Don,t Enter alnums , string and symbols as bank employee id")
    def AllCustomer(self):
        try:
            conn = mysql_connection()
            cur = conn.cursor()
            qu = "select * from Customer_Info "
            cur.execute(qu)
            print("-" * 100)
            for colinfo in cur.description:
                print("\t{}".format(colinfo[0]), end="\t\t")
            print()
            print("-" * 100)
            records = cur.fetchall()
            for record in records:
                for val in record:
                    print("\t{}".format(val), end="\t")
                print()
            print("-" * 100)
        except mysql.connector.DatabaseError as db:
            print("Please wait, there is a problem in database we shortly sort out this problem !")







