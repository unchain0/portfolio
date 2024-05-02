import unittest
from datetime import date

from sistema_bancario.v2.scripts.conta_corrente import ContaCorrente
from sistema_bancario.v2.scripts.errors import DuplicateError
from sistema_bancario.v2.scripts.usuario import Usuario


class TestContaCorrente(unittest.TestCase):
    def setUp(self):
        ContaCorrente.lista_contas = []
        Usuario.lista_usuarios = []
        self.nome = 'Arthur'
        self.nascimento = date(day=6, month=1, year=1999)
        self.endereco = 'logradouro, 01 - bairro - cidade/SP'
        self.cpf = '12345678903'
        self.user = Usuario.criar_usuario(
            self.nome,
            self.nascimento,
            self.cpf,
            self.endereco
        )
        self.conta_num_corr = 1
        self.conta_num_incorr = [1, '123', 'abcd']

        self.conta_1 = ContaCorrente.criar_conta(self.user, self.conta_num_corr)

    def test_validar_usuario(self):
        with self.assertRaises(DuplicateError):
            ContaCorrente.criar_conta(self.user, 2)

    def test_validar_numero_conta(self):
        for conta_num in self.conta_num_incorr:
            with self.subTest(conta_num=conta_num):
                with self.assertRaises((DuplicateError, TypeError)):
                    ContaCorrente.criar_conta(self.user, conta_num)


if __name__ == '__main__':
    unittest.main()
