from abc import ABC
from datetime import date

from .transaction import Transaction


class NaturalPerson(ABC):
    def __init__(self, cpf: str, name: str, birth_date: date):
        self.__cpf = cpf
        self.__name = name
        self.__birth_date = birth_date

    @property
    def cpf(self):
        return self.__cpf

    @property
    def name(self):
        return self.__name

    @property
    def birth_date(self):
        return self.__birth_date


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
