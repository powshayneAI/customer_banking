from Accounts import Account

def create_savings_account(balance, interest_rate, months):
    account_instance = Account(balance, interest_rate)
    interest_earned = balance * (interest_rate / 100 * months / 12)

    account_instance.set_balance(balance)
    account_instance.set_interest_rate(0)

    new_balance = balance + interest_earned

    account_instance.set_balance(new_balance)
    account_instance.set_interest_rate(interest_earned)

    return new_balance, interest_earned