from savings_account import create_savings_account
from cd_account import create_cd_account

#prompt user for starting balance

def main():
    balance = float(input('Enter your starting balance: '))
    interest_rate = float(input('Enter your annual interest rate: '))
    months = int(input('Enter the amount of months that your account has existed: '))

    new_balance, interest_earned = create_savings_account(balance, interest_rate, months)

    print(f"This is the interest earned: ${interest_earned:,.2f}. This is your updated savings: ${new_balance:,.2f} after the past {month} months.")

    cd_balance = float(input('Please enter a balance for your CD account: '))
    cd_interest_rate = float(input('Please enter your CD interest rate: '))
    cd_months = int(input('Please enter how many months you have had your CD account: '))

    new_balance, interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    print(f"This is the interest earned: ${interest_earned:,.2f}. This is your updated savings: ${new_balance:,.2f} after the past {month} months.")

if __name__ == "__main__":
    main()