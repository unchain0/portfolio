from datetime import date

from models.checking_account import CheckingAccount
from models.customer import Customer
from models.exceptions import InvalidOptionError

customer = Customer(
    cpf="123.456.789-00",
    name="John Doe",
    birth_date=date(2000, 1, 1),
    address="123 Main St",
)
account = CheckingAccount(
    number=1,
    customer=customer,
)
menu = """
[d] Deposit
[w] Withdraw
[t] Transactions
[e] Exit

=> """

while True:
    try:
        option = input(menu).strip()[0]
        match option:
            case "d":
                amount = float(input("Amount to deposit: $"))
                account.deposit(amount)
            case "w":
                amount = float(input("Amount to withdraw: $"))
                account.withdraw(amount)
            case "t":
                account.historic.print_transactions(balance=account.balance)
            case "e":
                raise KeyboardInterrupt
            case _:
                raise InvalidOptionError()
    except (IndexError, InvalidOptionError):
        print("@@@ Operation failed! Invalid option. @@@")
    except (TypeError, ValueError) as e:
        print(f"@@@ Operation failed! {e} @@@")
    except KeyboardInterrupt:
        print("\n=== Leaving ===")
        break
