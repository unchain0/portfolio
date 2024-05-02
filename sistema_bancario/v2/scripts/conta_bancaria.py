from abc import ABC
from typing import Literal

from colorama import Fore, Style


class ContaBancaria(ABC):
    LIMITE_SAQUE: float = 500.0
    MAX_SAQUES: int = 3
    id_: int = 1

    def __init__(self):
        self.id = self.id_
        self.id_ += 1
        self.saldo = 0
        self.__extrato = ""
        self.numero_saques = 0

    def deposito(self, valor: float, /) -> None:
        if self._validar_valor(valor):
            self._atualizar_saldo(valor)
            self._atualizar_extrato("Depósito", valor, Fore.GREEN)
        self.imprimir_extrato()

    def saque(self, *, valor: float) -> None:
        if self._validar_valor(valor) and self._validar_saque(valor):
            self._atualizar_saldo(-valor)
            self._atualizar_extrato("Saque", valor, Fore.RED)
            self.numero_saques += 1
        self.imprimir_extrato()

    @staticmethod
    def _validar_valor(valor: float) -> bool:
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False
        return True

    def _validar_saque(self, valor: float) -> bool:
        if valor > self.saldo:
            print("Você não tem saldo suficiente.")
            return False
        if valor > self.LIMITE_SAQUE:
            print(f"O valor do saque excede o limite. (R$ {self.LIMITE_SAQUE:.2f})")
            return False
        if self.numero_saques >= self.MAX_SAQUES:
            print(f"Número máximo de saques excedido. ({self.MAX_SAQUES})")
            return False
        return True

    def _atualizar_saldo(self, valor) -> None:
        self.saldo += valor

    def _atualizar_extrato(self, operacao: Literal["Depósito", "Saque"], valor: float, cor) -> None:
        self.__extrato += f"{cor}{operacao}: R$ {valor:.2f}{Style.RESET_ALL}\n"

    def imprimir_extrato(self) -> None:
        print("\n================ EXTRATO ================")
        print(
            "Não foram realizadas movimentações.\n"
            if not self.__extrato
            else self.__extrato
        )
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("==========================================")
