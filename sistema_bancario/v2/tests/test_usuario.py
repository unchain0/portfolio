import unittest
from datetime import date, timedelta

import sistema_bancario.v2.scripts.errors as err
from sistema_bancario.v2.scripts.conta_corrente import ContaCorrente
from sistema_bancario.v2.scripts.usuario import Usuario


class TestUsuario(unittest.TestCase):
    def setUp(self):
        Usuario.lista_usuarios = []
        self.nome = 'Arthur'
        self.nascimento = date(day=6, month=1, year=1999)
        self.endereco_corr = 'logradouro, 01 - bairro - cidade/SP'
        self.endereco_incorr = [
            'logradouro, 01 bairro cidade/SP',
            'logradouro 01 bairro cidade/SP',
            'logradouro, 01 - bairro cidade/SP',
            'logradouro,01-bairro-cidade/SP',
            'logradouro, 01 - bairro - cidade/SPJ'
        ]
        self.cpf_corr = '12345678903'
        self.cpf_incorr = ['123452', '12345678905', 'a1b2c3d4e5f6g7h8i9j0k1l']
        self.user_1 = Usuario.criar_usuario(
            'Felippe',
            date(day=5, month=3, year=2001),
            '12345678905',
            self.endereco_corr
        )
        self.user_2 = Usuario.criar_usuario(
            self.nome,
            self.nascimento,
            self.cpf_corr,
            self.endereco_corr
        )
        ContaCorrente.lista_contas = []
        self.conta_1 = ContaCorrente.criar_conta(self.user_1, 1)
        self.conta_2 = ContaCorrente.criar_conta(self.user_2, 2)

    def test_validar_cpf(self):
        for cpf in self.cpf_incorr:
            with self.subTest(cpf=cpf):
                with self.assertRaises((err.LenError, err.DuplicateError, TypeError)):
                    Usuario.criar_usuario(self.nome, self.nascimento, cpf, self.endereco_corr)

    def test_validar_endereco(self):
        for endereco in self.endereco_incorr:
            with self.subTest(endereco=endereco):
                with self.assertRaises(err.AddressFormatError):
                    Usuario.criar_usuario(self.nome, self.nascimento, self.cpf_corr, endereco)

    def test_validar_conta_bancaria(self):
        self.user_1.conta = self.conta_1
        self.user_1.conta = self.conta_2
        with self.assertRaises(err.DuplicateError):
            self.user_2.conta = self.conta_1
        with self.assertRaises(err.DuplicateError):
            self.user_2.conta = self.conta_2

    def test_validar_data_nascimento(self):
        with self.assertRaises(err.FutureDateError):
            now = date.today()
            Usuario.validar_data_nascimento(now + timedelta(days=10))


if __name__ == '__main__':
    unittest.main()
