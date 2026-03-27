class bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("account deposited with amount: ", amount)
        else:
            print("invalid amount")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("account withdrawn with amount: ", amount)
        else:
            print("insufficient balance")


class ATM(bankaccount):
    def show_details(self):
        print("\n account details: ")
        print("name: ", self.name) 
        print("balance: ", self.get_balance)

account1 = ATM("sanjay", 1000)
account1.show_details()
account1.deposit(500)
account1.withdraw(200)
account1.show_details()