from datetime import date

from scripts.conta_corrente import ContaCorrente
from scripts.usuario import Usuario

user = Usuario.criar_usuario(
    'Felippe',
    date(day=5, month=3, year=2001),
    '12345678901',
    'logradouro, 01 - bairro - cidade/RJ'
)
conta = ContaCorrente.criar_conta(usuario=user, numero_conta=1)
menu = """
[d] Depositar
[s] Sacar
[q] Sair

=> """

while True:
    try:
        opcao = input(menu).strip().lower()
        match opcao:
            case "d":
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    conta.deposito(valor)
                except ValueError as e:
                    print(e)
            case "s":
                try:
                    valor = float(input("Informe o valor do saque: "))
                    conta.saque(valor=valor)
                except ValueError as e:
                    print(e)
            case "q":
                break
            case _:
                print("Operação inválida, selecione a operação desejada novamente.")
    except ValueError:
        print("Valor inválido! Forneça um valor numérico.")
    except KeyboardInterrupt:
        print("\nEncerrando...")
        break
