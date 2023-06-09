from User import User
from Bank import Bank
from Admin import Admin


def main():
    bank = Bank("Duch Bangla Bank", "Bangladesh")

    # adding user from bank
    user1 = User("Md.Al-Amin", "alamin@gmail.com", "1234", 1000)
    bank.add_account(user1)

    user2 = User("Najmul Islam", "najmul@gmail.com", "45678", 5000)
    bank.add_account(user2)

    # user can create account by themselves
    user3 = User("Summon Molla", "sumon@gmail.com", "adbdsc", 7000)
    user3.create_account(bank)

    # bank.list_accounts()
    print("_____________________________________________________\n")

    # user can deposit money
    user1.deposit_money(bank, 1070)
    user1.deposit_money(bank, 4000)
    user1.withdraw_money(bank, 1000)
    user1.withdraw_money(bank, 2000)
    user1.deposit_money(bank, 3000)
    user1.transfer_money(user2, 1000, bank.total_balance)

    bank.provide_loan(user3, 1400, 10, 2)

    # print("-------------- Transaction History --------------")
    # user1.get_transaction_history()
    # user2.get_transaction_history()

    bank.make_admin(user1)

    user4 = Admin("Kabir Islam", "kabir@gmail.com", "54967", 1000)
    user4.create_admin_account(bank)

    print(f"Total Bank Balance: {user4.total_bank_balance(bank)}")
    # print(f"Total Bank Loan: {bank.total_balance}")
    print(f"Total Bank Loan: {user4.total_bank_loan(bank)}")
    # print(f"Total Bank Loan: {bank.total_loan}")
    user4.change_loan_availability(bank, False)
    print(f"Is loan available: {bank.is_loan_available}")

    bank.list_accounts()


if __name__ == "__main__":
    main()