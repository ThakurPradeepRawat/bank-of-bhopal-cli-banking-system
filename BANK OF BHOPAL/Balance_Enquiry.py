from Exceptions import InvalidFund,InvalidPinError,InsufficientFundError
from Validations import Validation
class Balance:
    def account_info(self):
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
                    self.current_bal = Validation.remaining_balance(self)
                    print("-" * 100)
                    print("Account Number :- {}".format(self.acc_no))
                    print("Available Balance :- {}".format(self.current_bal))
                    print("-" * 100)
        except ValueError:
            print("Don't enter alnum, str , and special symbols ")
        except InvalidPinError:
            print("Please enter valid account pin !")