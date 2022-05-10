class BankATM:
    def __init__(self,password,cardnumber):
        self.password = password
        self.cardnumber = cardnumber

    def check_balance(self):
        print("Your balance is 200000")

    def withdrawal(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn ₹"+str(amount)+ ", Your balance is" + " ₹"+str(new_amount))


def functions():
    Card_number = input("Insert your card number: ")
    Password  = input("Enter your password number: ")

    new_user =  BankATM(Card_number ,Password)

    print("Choose your activity")
    print("1.Balance Enquiry   2.Withdrawal")
    activityNumber = int(input("Enter activity number: "))

    if (activityNumber == 1):
        new_user.check_balance()
    elif (activityNumber == 2):
        amount = int(input("Enter the amount: "))
        new_user.withdrawal(amount)
    else:
        print("Enter a valid number: ")

functions()