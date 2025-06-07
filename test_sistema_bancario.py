
import unittest
from sistema_bancario_poo import Usuario, ContaBancaria, Banco

class TestSistemaBancario(unittest.TestCase):

    def setUp(self):
        self.banco = Banco()
        self.usuario = Usuario("João Silva", "12345678900", "01-01-1990", "Rua A, 123 - Centro - Cidade/UF")
        self.banco.usuarios.append(self.usuario)
        self.conta = ContaBancaria("0001", 1, self.usuario)
        self.banco.contas.append(self.conta)

    def test_cadastro_usuario(self):
        novo_usuario = Usuario("Maria Souza", "98765432100", "02-02-1985", "Rua B, 456 - Bairro - Cidade/UF")
        self.banco.usuarios.append(novo_usuario)
        self.assertIn(novo_usuario, self.banco.usuarios)

    def test_criacao_conta(self):
        nova_conta = ContaBancaria("0001", 2, self.usuario)
        self.banco.contas.append(nova_conta)
        self.assertIn(nova_conta, self.banco.contas)

    def test_deposito_valido(self):
        self.conta.depositar(1000)
        self.assertEqual(self.conta.saldo, 1000)

    def test_deposito_invalido(self):
        self.conta.depositar(-50)
        self.assertEqual(self.conta.saldo, 0)

    def test_saque_valido(self):
        self.conta.depositar(1000)
        self.conta.sacar(200)
        self.assertEqual(self.conta.saldo, 800)

    def test_saque_acima_limite(self):
        self.conta.depositar(1000)
        self.conta.sacar(600)
        self.assertEqual(self.conta.saldo, 1000)

    def test_saque_sem_saldo(self):
        self.conta.sacar(100)
        self.assertEqual(self.conta.saldo, 0)

    def test_limite_saques(self):
        self.conta.depositar(1500)
        for _ in range(3):
            self.conta.sacar(100)
        self.conta.sacar(100)  # 4º saque não deve ser permitido
        self.assertEqual(self.conta.saldo, 1200)

    def test_extrato(self):
        self.conta.depositar(500)
        self.conta.sacar(200)
        extrato = self.conta.gerar_extrato()
        self.assertIn("Depósito: R$ 500.00", extrato)
        self.assertIn("Saque: R$ 200.00", extrato)
        self.assertIn("Saldo atual: R$ 300.00", extrato)

if __name__ == "__main__":
    unittest.main()
