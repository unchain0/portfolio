from .account import Account


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
