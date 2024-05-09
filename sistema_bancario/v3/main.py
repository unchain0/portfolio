from datetime import date

from faker import Faker

from models.checking_account import CheckingAccount
from models.customer import Customer
from models.exceptions import InvalidOptionError

fake = Faker()
customer = Customer(
    cpf="12345678901",
    name=fake.name(),
    birth_date=date(2000, 1, 1),
    address=fake.address(),
)
account = CheckingAccount(1, customer)
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
