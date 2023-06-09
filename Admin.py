from User import User


class Admin(User):
    def __init__(self, name, email, password, balance) -> None:
        super().__init__(name, email, password, balance)

    def create_user_account(self, bank):
        bank.add_account(self)

    def create_admin_account(self, bank):
        bank.add_account(self)
        self.role = "Admin"

    def make_admin(self, user):
        if self.role == "Admin":
            user.role = "Admin"
        else:
            print("Unauthorized")

    def total_bank_balance(self, bank):
        if self.role == "Admin":
            return bank.total_balance
        else:
            return "Unauthorized"

    def total_bank_loan(self, bank):
        return bank.total_loan

    def change_loan_availability(self, bank, is_loan_available=True):
        bank.is_loan_available = is_loan_available