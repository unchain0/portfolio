from conta_bancaria import ContaBancaria

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
conta = ContaBancaria()

while True:
    opcao = input(menu).lower()

    try:
        match opcao:
            case "d":
                valor = float(input("Informe o valor do depósito: "))
                conta.deposito(valor)
            case "s":
                valor = float(input("Informe o valor do saque: "))
                conta.saque(valor)
            case "e":
                conta.extrato()
            case "q":
                break
            case _:
                print(
                    "Operação inválida, por favor selecione novamente a operação desejada."
                )
    except ValueError:
        print("Valor inválido! Por favor, informe um valor numérico.")
