lst_num = ['Data', 'Science', 'Academy', 'Nota', 10, 10]
print(type(lst_num))
print(type([]))

print(lst_num.count(10))
print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))

class Carro(object):
    pass

ferrari = Carro()
print(type(ferrari))


class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


Estudante1 = Estudantes("Bob", 12, 9.5)
print(f'{Estudante1.nome} tem {Estudante1.idade} anos e tirou a nota: {Estudante1.nota}.')


class Funcionarios:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    

    def listFunc(self):
        print(f'Funcionário(a) {self.nome} tem salário de R$ {self.salario:.2f} e o cargo é {self.cargo}.')


Func1 = Funcionarios('Mary', 20000, 'Cientista de Dados')
Func1.listFunc()
print('*** Usando atributos ***')
print(hasattr(Func1, 'nome'))
print(hasattr(Func1, 'salario'))
print(f'{Func1.nome}, R$ {Func1.salario:.2f}.')
setattr(Func1, 'salario', 4500)
print(hasattr(Func1, 'salario'))
print(Func1.salario)
print(getattr(Func1, 'salario'))
delattr(Func1, 'salario')
print(hasattr(Func1, 'salario'))