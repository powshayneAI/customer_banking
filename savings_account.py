from Accounts import Account

create_savings_account(balance, interest):
    account_instance = Account(balance, interest)
    interest_earned = balance * (interest / 100)

    account_instance.set_balance(balance)
    account_instance.set_interest(0)

    new_balance = balance + interest_earned

    account_instance.set_balance(new_balance)
    account_instance.set_interest(interest_earned)

    return new_balance, interest_earned