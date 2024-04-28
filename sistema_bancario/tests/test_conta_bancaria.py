import unittest
from io import StringIO
from unittest.mock import patch

from sistema_bancario.conta_bancaria import ContaBancaria


class ContaBancariaTest(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, function, stdout):
        function()
        self.assertEqual(stdout.getvalue(), expected_output)

    def test_deposito(self):
        self.conta.deposito(100)
        self.assertEqual(self.conta.saldo, 100)

        self.assert_stdout(
            'Operação falhou! O valor informado é inválido.\n',
            lambda: self.conta.deposito(-100)
        )

    def test_saque(self):
        self.conta.deposito(1000)

        self.assert_stdout(
            'Operação falhou! O valor do saque excede o limite. (R$ 500.00)\n',
            lambda: self.conta.saque(600)
        )

        self.assert_stdout(
            'Operação falhou! O valor informado é inválido.\n',
            lambda: self.conta.saque(-1)
        )

        self.assert_stdout(
            'Operação falhou! Você não tem saldo suficiente.\n',
            lambda: self.conta.saque(2000)
        )

        self.conta.saque(100)
        self.assertEqual(self.conta.saldo, 900)
        self.assertEqual(self.conta.numero_saques, 1)

        self.conta.saque(100)
        self.conta.saque(100)
        self.assert_stdout(
            'Operação falhou! Número máximo de saques excedido. (3)\n',
            lambda: self.conta.saque(100)
        )

    def test_extrato(self):
        self.conta.extrato()


if __name__ == '__main__':
    unittest.main()
