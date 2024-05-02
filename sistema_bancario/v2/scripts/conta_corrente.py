import sistema_bancario.v2.scripts.errors as err
from .conta_bancaria import ContaBancaria
from .usuario import Usuario


class ContaCorrente(ContaBancaria):
    lista_contas: list['ContaCorrente'] = []
    agencia: str = "0001"

    def __init__(self, usuario: Usuario, numero_conta: int):
        self.__numero_conta = numero_conta
        self.__usuario = usuario
        super().__init__()

    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def usuario(self):
        return self.__usuario

    @classmethod
    def criar_conta(cls, usuario: Usuario, numero_conta: int) -> 'ContaCorrente':
        cls.__validar_numero_conta(numero=numero_conta)
        cls.__validar_usuario(user=usuario)
        temp_conta = cls(usuario, numero_conta)
        cls.lista_contas.append(temp_conta)
        return temp_conta

    @classmethod
    def __validar_numero_conta(cls, numero: int) -> None:
        if not isinstance(numero, int):
            raise TypeError(f"O número da conta '{numero}' é inválido.")
        for conta in cls.lista_contas:
            if conta.numero_conta == numero:
                raise err.DuplicateError(f"O número da conta '{conta.numero_conta}' já existe na lista de contas.")

    @classmethod
    def __validar_usuario(cls, user: Usuario) -> None:
        for conta in cls.lista_contas:
            if conta.usuario == user:
                raise err.DuplicateError(f"O usuário '{user.nome}' já existe na lista de contas.")
