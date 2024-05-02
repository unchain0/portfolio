class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.__extrato = ""
        self.numero_saques = 0

    def deposito(self, valor: float) -> None:
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            self.saldo += valor
            self.__extrato += f"Depósito: R$ {valor:.2f}\n"

    def saque(self, valor: float) -> None:
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES
        valor_invalido = valor <= 0

        if any([excedeu_saldo, excedeu_limite, excedeu_saques, valor_invalido]):
            print("Operação falhou!", end=" ")

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"O valor do saque excede o limite. (R$ {self.limite:.2f})")
        elif excedeu_saques:
            print(f"Número máximo de saques excedido. ({self.LIMITE_SAQUES})")
        elif valor <= 0:
            print("O valor informado é inválido.")
        else:
            self.saldo -= valor
            self.__extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1

    def extrato(self) -> None:
        print("\n================ EXTRATO ================")
        print(
            "Não foram realizadas movimentações."
            if not self.__extrato
            else self.__extrato
        )
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("==========================================")
