# Bank System UML Documentation

## Classes and Interfaces

### Customer

- **Attributes**
    - `address: str`
    - `accounts: list`
- **Methods**
    - `perform_transaction(account: Account, transaction: Transaction) -> None`
    - `add_account(account: Account) -> None`

### NaturalPerson (inherits Client)

- **Attributes**
    - `cpf: str`
    - `name: str`
    - `birth_date: date`

### Account

- **Attributes**
    - `balance: float`
    - `number: int`
    - `agency: str`
    - `customer: Customer`
    - `history: History`
- **Methods**
    - `new_account(customer: Customer, number: int) -> Account`
    - `withdraw(amount: float) -> bool`
    - `deposit(amount: float) -> bool`

### CheckingAccount (inherited Account)

- **Attributes**
    - `limit: float`
    - `withdrawals_limit: int`

### History

- **Attributes**
    - `transactions: list`
- **Methods**
    - `add_transaction(transaction: Transaction) -> None`

### Transaction (Interface)

- **Attributes**
    - `amount: float`
- **Methods**
    - `register(account: Account) -> None`

### Deposit (implements Transaction)

- **Methods**
    - `register(account: Account) -> None`

### Withdrawal (implements Transaction)

- **Methods**
    - `register(account: Account) -> None`
