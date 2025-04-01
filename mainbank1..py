class BankAccount:                                                                    # Created a base class or Parent class.
    def __init__(self, account_number, balance):                                      # Created a function and in that we used account_number, for encapsulation we used__to protect it.
        self.__account_number = account_number                                        # To get the account number.
        self.__balance = balance                                                      # To get the balance.
    def deposit(self, amount):                                                        # Used another function called deposit.
        self.__balance += amount

        return f"deposit {amount} new balance {self.__balance}"                       # Here we will get deposit and ans the new amount.

    def withdraw(self, amount):                                                       # Created a new  function called withdraw.
        if amount <= self.__balance:
            self.__balance -= amount
            return f" withdrawn amount is {amount} new balance {self.__balance}"      # It will return withdrawn amount.
        else:
            return "insufficient funds"                                               # It will return insufficient balance if amount is lees than it required.
    def get_balance(self):
            return self.__balance

class SavingsAccount(BankAccount):                                                    # Created a child class using parent class BankAccount.
    interest_rate = 0.03
    def __init__(self, account_number, balance, interest_rate):
     super().__init__(account_number, balance)                                        # Used to refer the parent class.
     self.__interest_rate = interest_rate

    def calculate_interest(self):                                                     # Here we calculate the interest.
            return f"interest amount rate: {self.get_balance() * self.__interest_rate}"

class CurrentAccount(BankAccount):                                                    # Created a child class using Parent class.
    def __init__(self,  account_number, min_balance, balance):
        super().__init__(account_number,min_balance)                                  # Take's Refer from its parent class.
        self.__min_balance = min_balance
    def min_balance(self):
        return f"minimum balance must be {self.__min_balance * 2}"                    # Return's the minimum balance.

account1 = BankAccount("443780000076", 10000)                    # We are giving  the account and balance in account1.
print(account1.deposit(4000))                                                         # Used to deposit the amount.
print(account1.withdraw(2000))                                                        # Used withdrawn the account.
Savings = SavingsAccount("564639930047", 40000, 0.03) # Creating the savings account to Display the output.
print(Savings.calculate_interest())
current = CurrentAccount("98765425", 10000, 2000)     # Used to display the output of current account.
print(current.min_balance())
print(current.withdraw(400000))








