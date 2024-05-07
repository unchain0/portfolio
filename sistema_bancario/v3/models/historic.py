from abc import ABC
from datetime import datetime
from typing import List, TypedDict

from .transaction import Transaction


class TransactionDict(TypedDict):
    type: str
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

    def print_transactions(self, balance: float) -> None:
        print("================ TRANSACTIONS ================")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print(f"{t['type']} of ${t['amount']:.2f} at {t['date']}")
        print(f"\nBalance: ${balance:.2f}")
        print("==============================================")
