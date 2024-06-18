from Accounts import Account

create_savings_account(balance, interest_rate):
    account_instance = Account(balance, interest_rate)
    interest = balance * (interest_rate / 100)

    account_instance.set_balance(new_balance)

    account_instance.set_interest(interest)

    new_balance = balance + interest

    return new_balance, interest