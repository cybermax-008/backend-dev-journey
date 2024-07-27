class BankAccount:
    overdraft_limit = 1000
    def __init__(self, full_name , opening_balance):
        self.full_name = full_name
        self._balance = opening_balance
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    @property
    def available_balance(self):
        return self._balance + self.overdraft_limit

    def deposit(self, amt):
        if amt > 0:
            self._balance += amt
            self.transactions.append(f"Deposited :{amt}")
            return f"Deposited {amt} and New balance {self._balance}"
        else:
            return "invalid deposit amount"

    def withdrawal(self, amt):
        if amt >0:
            if self.available_balance >= amt:
                self._balance -= amt
                self.transactions.append(f"Withdrawal: {amt}")
                return f"Withdrew {amt} and New balance {self._balance}"
            else:
                return f"Requested amount is unavailable, max withdrawal {self.available_balance}"
        else:
            return "invalid withdrawal amount"

    def get_statement(self):
        return "\n".join(self.transactions)

    def balance_enquiry(self):
        return f" Available balance {self.available_balance} and Actual balance {self.balance}"
    

customer_1 = BankAccount("Surya M", 1000)
print(customer_1.withdrawal(200))
print(customer_1.balance_enquiry())
print(customer_1.withdrawal(1500))
print(customer_1.balance_enquiry())
print(customer_1.deposit(500))
print(customer_1.get_statement())