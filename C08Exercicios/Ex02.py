# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

        print('Pessoa cadastrada:')

    
    def mostra(self):
        print(f'Nome: {self.nome}\nCidade: {self.cidade}\nTelefone: {self.telefone}\nE-mail: {self.email}')

    
p1 = Pessoa('João', 'Brasília', '61 99999-9999', 'joaozin@hotmail.com')
p1.mostra()