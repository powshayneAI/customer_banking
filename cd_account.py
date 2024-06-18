from Accounts import Account

def create_cd_account(cd_balance, cd_interest_rate, cd_months):
    account_instance =  Account(cd_balance, cd_interest_rate)
    interest_earned = cd_balance * (cd_interest_rate / 100 * cd_months / 12)

    account_instance.set_balance(cd_balance)
    account_instance.set_interest_rate(interest_earned)

    new_balance = cd_balance + interest_earned

    account_instance.set_balance(new_balance)

    return new_balance, interest_earned
