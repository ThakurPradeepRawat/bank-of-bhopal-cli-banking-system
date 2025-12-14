from Exceptions import RangeError
from Account import Account
from Deposit import Deposit
from Withdraw import Withdraw
from Balance_Enquiry import Balance
from CustomerInfo import CustomerInfo
from Update_Pin import Pin
from Customer import Bank
class Menu:
    @staticmethod
    def perform():
        print("*" * 100)
        print("\t\t\tWhat you want ?")
        print("*" * 100)
        print("1. Create account ")
        print("2. Deposit ")
        print("3. Withdraw")
        print("4. Balance Enquiry")
        print("5. Account Information ")
        print("6. Pin Update")
        print("7. Bank Customers Detail ")
        print("8. Exit ")
        print("-" * 100)
class Choose:

    def get_choice(self):

        while (True):

            try:
                Menu.perform()
                print("-" * 100)
                self.choice = int(input("Enter your Choice :- "))
                if self.choice < 1 or self.choice > 8:
                    raise RangeError
                print("-" * 100)
            except ValueError:
                print("Don't Enter other than (1-8) in choice ")
            except RangeError:
                print("Please enter choice from 1 - 8 .")
            else:
                self.operation()
                break
    def operation_choice(self):
        self.c = input("Do you want to perform another operation (yes/no) :")
        if self.c.lower() =="no":
            print("-"*100)
            print("\tThanks for using BANK OF BHOPAL ATM service !")
            print("-" * 100)
        else:
            self.get_choice()
    def operation(self):
        match (self.choice):
            case 1:
                user = Account()
                user.accountDetail()
                user.create_account()
                self.operation_choice()

            case 2:
                d = Deposit()
                d.account_info()
                self.operation_choice()

            case 3:
                w = Withdraw()
                w.account_validation()
                self.operation_choice()
            case 4:
                b = Balance()
                b.account_info()
                self.operation_choice()

            case 5:
                c = CustomerInfo()
                c.accInfo()
                self.operation_choice()
            case 6:
                p=Pin()
                p.accInfo2()
                self.operation_choice()
            case 7:
                B = Bank()
                B.checkemployee()
                self.operation_choice()
            case 8:
                print("Thanks for using BANK OF BHOPAL ATM service ! ")
                print("="*100)









