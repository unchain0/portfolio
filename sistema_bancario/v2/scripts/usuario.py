import re
from datetime import date

import sistema_bancario.v2.scripts.errors as err
from .conta_bancaria import ContaBancaria


class Usuario:
    lista_usuarios: list['Usuario'] = []

    def __init__(self, nome: str, data_nascimento: date, cpf: str, endereco: str, conta: list[ContaBancaria] = None):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__endereco = endereco
        if conta is None:
            self.__conta = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def endereco(self) -> str:
        return self.__endereco

    @property
    def conta(self) -> list[ContaBancaria]:
        return self.__conta

    @conta.setter
    def conta(self, conta_bancaria: ContaBancaria) -> None:
        self.validar_conta_bancaria(user=self, conta_bancaria=conta_bancaria)
        self.__conta.append(conta_bancaria)

    @classmethod
    def criar_usuario(cls, nome: str, data_nascimento: date, cpf: str, endereco: str) -> 'Usuario':
        cls.validar_endereco(endereco)
        cls.validar_data_nascimento(data_nascimento)
        cls.validar_cpf(cpf)
        temp_user = cls(nome, data_nascimento, cpf, endereco)
        cls.lista_usuarios.append(temp_user)
        return temp_user

    @classmethod
    def validar_endereco(cls, endereco: str) -> None:
        pattern = r"^.+, \s*\d+\s* - \s*.+\s* - \s*.+\/\D{2}$"
        if not re.match(pattern, endereco):
            raise err.AddressFormatError(
                "Endereço inválido: deve seguir o formato 'logradouro, nro - bairro - cidade/sigla_estado'")

    @classmethod
    def validar_data_nascimento(cls, data_nascimento: date) -> None:
        if data_nascimento > date.today():
            raise err.FutureDateError("Data de nascimento não pode ser uma data futura")

    @classmethod
    def validar_cpf(cls, cpf: str) -> None:
        if not cpf.isdigit():
            raise TypeError("CPF inválido: deve conter apenas números.")
        if len(cpf) != 11:
            raise err.LenError("CPF inválido: deve conter exatamente 11 dígitos.")
        for usr in cls.lista_usuarios:
            if usr.cpf == cpf:
                raise err.DuplicateError(f"O CPF {cpf!r} já existe na lista de usuários.")

    @classmethod
    def validar_conta_bancaria(cls, user: 'Usuario', conta_bancaria: ContaBancaria) -> None:
        for user in cls.lista_usuarios:
            if conta_bancaria in user.conta:
                raise err.DuplicateError(f"A conta de id {conta_bancaria.id!r} já existe neste usuário.")
