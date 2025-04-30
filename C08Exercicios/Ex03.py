# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

        print('Smartphone criado.')

    
    def imprimir(self):
        pass
        


class MP3player(Smartphone):
    def __init__(self, tamanho, interface, capacidade):
        super().__init__(tamanho, interface)
        self.capacidade = capacidade

    
    def imprimir(self):
        print(f'Tamanho: {self.tamanho}\nInterface: {self.interface}\nCapacidade: {self.capacidade}')


smart = MP3player('6 polegadas', 'IOS', '128GB')
smart.imprimir()