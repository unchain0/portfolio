from abc import ABC, abstractmethod


class Transaction(ABC):
    def __init__(self, amount: float):
        self.__amount = amount

    @property
    def amount(self) -> float:
        return self.__amount

    @abstractmethod
    def register(self, account) -> None:
        pass


class Withdraw(Transaction):
    def register(self, account: "Account") -> None:
        valid_transaction = account.withdraw(self.amount)
        if valid_transaction:
            account.historic.add_transaction(self)


class Deposit(Transaction):
    def register(self, account: "Account") -> None:
        valid_transaction = account.deposit(self.amount)
        if valid_transaction:
            account.historic.add_transaction(self)
