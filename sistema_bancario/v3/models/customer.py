from abc import ABC

from .natural_person import NaturalPerson
from .transaction import Transaction


class Customer(NaturalPerson, ABC):
    def __init__(self, cpf, name, birth_date, address: str):
        super().__init__(cpf, name, birth_date)
        self.__address = address
        self.__accounts: list = []

    @property
    def address(self):
        return self.__address

    @property
    def accounts(self):
        return self.__accounts

    @staticmethod
    def perform_transaction(account, transaction: Transaction) -> None:
        transaction.register(account)

    def add_account(self, account) -> None:
        self.accounts.append(account)
