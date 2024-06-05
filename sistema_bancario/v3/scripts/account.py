from abc import ABC

from .customer import Customer
from .historic import Historic
from .transaction import Withdraw, Deposit


class Account(ABC):

    def __init__(self, number: int, customer: Customer):
        self.__number = number
        self.__customer = customer
        self.__balance: float = 0
        self.__agency: str = "0001"
        self.__historic: Historic = Historic()

    @property
    def balance(self):
        return self.__balance

    @property
    def number(self):
        return self.__number

    @property
    def agency(self):
        return self.__agency

    @property
    def customer(self):
        return self.__customer

    @property
    def historic(self):
        return self.__historic

    @classmethod
    def new_account(cls, customer: "Customer", number: int) -> "Account":
        return cls(number, customer)

    def withdraw(self, amount: float) -> bool:
        if not isinstance(amount, (float, int)):
            print("@@@ Operation failed! The provided value is invalid. @@@")
        elif amount < 20:
            print("@@@ Operation failed! The minimum withdrawal is $20 @@@")
        elif amount > self.balance:
            print(
                "@@@ Operation failed! You do not have sufficient balance. @@@"
            )
        else:
            self.__balance -= amount
            self.historic.add_transaction(transaction=Withdraw(amount))
            print("=== Withdrawal successfully completed! ===")
            return True
        return False

    def deposit(self, amount: float) -> bool:
        if amount < 25:
            print("@@@ Operation failed! The minimum deposit is $25 @@@")
        else:
            self.__balance += amount
            self.historic.add_transaction(transaction=Deposit(amount))
            print("=== Deposit successfully completed! ===")
            return True
        return False


class CheckingAccount(Account):
    def __init__(
            self,
            number,
            customer,
            limit: float = 500,
            withdrawals_limit: int = 3,
    ):
        super().__init__(number, customer)
        self.__limit = limit
        self.__withdrawals_limit = withdrawals_limit

    @property
    def limit(self):
        return self.__limit

    @property
    def limit_withdrawals(self):
        return self.__withdrawals_limit

    def withdraw(self, amount: float) -> bool:
        number_withdrawals = len(
            [
                transaction
                for transaction in self.historic.transactions
                if transaction["type"] == "Withdraw"
            ]
        )

        if amount > self.limit:
            print(
                f"@@@ Operation failed! The withdrawal amount exceeds the limit (${self.limit:.2f}). @@@"
            )
        elif number_withdrawals >= self.limit_withdrawals:
            print(
                f"@@@ Operation failed! The number of withdrawals has reached the limit ({self.limit_withdrawals}). @@@"
            )
        else:
            return super().withdraw(amount)
        return False

    def __str__(self):
        return f"""\
        Agency:{self.agency:>30}
        C/C:{self.number:>30}
        Customer:{self.customer.name:>30}
        """
