from User import TrxHistory, LoanDetails


class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.accounts = []
        self.total_balance = 0
        self.total_loan = 0
        self.is_loan_available = True

    def add_account(self, user):
        self.accounts.append(user)
        self.total_balance += user.balance
        self.total_loan += user.loan
        obj = TrxHistory("own", user.balance, "Deposit")
        user.transaction_history.append(obj)

    def remove_account(self, user):
        self.accounts.remove(user)
        self.total_balance -= user.balance
        self.total_loan -= user.loan

    def make_admin(self, user):
        user.role = "Admin"

    def deposit(self, user, amount):
        res = False
        if amount > 0:
            user.balance += amount
            self.total_balance += amount

            res = True
        else:
            print("Invalid amount")

        return res

    def withdraw(self, user, amount):
        res = False
        if user.balance >= amount:
            if self.total_balance >= amount:
                user.balance -= amount
                self.total_balance -= amount

                res = True
            else:
                print("Bank is bankrupt")
        else:
            print("Insufficient balance")

        return res

    def provide_loan(self, user, amount, interest, duration):
        if self.total_balance >= amount:
            if self.is_loan_available and amount <= 2 * user.balance:
                user.loan += amount
                user.balance += amount
                self.total_balance -= amount
                self.total_loan += amount

                obj = LoanDetails(user.name, amount, interest, duration)
                user.loan_history.append(obj)
            else:
                print("Loan is not available")
        else:
            print("Bank is bankrupt")

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan(self):
        return self.total_loan

    def list_accounts(self):
        print("\n_____________All Accounts ______________________\n")
        for account in self.accounts:
            print(
                f"Name: {account.name} \nEmail: {account.email} \nBalance: {account.balance} \nLoan: {account.loan} \nRole: {account.role}"
            )
            print("____________________________________________________\n")