from abc import ABC
from datetime import datetime
from typing import List, TypedDict, Literal

from .transaction import Transaction


class TransactionDict(TypedDict):
    type: Literal["Withdraw", "Deposit"]
    amount: float
    date: str


class Historic(ABC):
    def __init__(self):
        self.__transactions: List[TransactionDict] = []

    @property
    def transactions(self) -> List[TransactionDict]:
        return self.__transactions[:]

    def add_transaction(self, transaction: Transaction) -> None:
        if isinstance(transaction, Transaction):
            self.__transactions.append(
                {
                    "type": transaction.__class__.__name__,
                    "amount": transaction.amount,
                    "date": datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
                }
            )
        else:
            raise TypeError("Invalid transaction type")
