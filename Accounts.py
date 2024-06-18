class Account:
    def __init__(self,balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    def set_balance(self, new_balance):
        self.balance = new_balance
    def set_interest_rate(self, new_interest_rate):
        self.interest_rate = new_interest_rate