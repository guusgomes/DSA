class Veiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    def acelerar(self):
        pass

    
    def frear(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f'O {self.marca} {self.modelo} está acelerando.')


    def frear(self):
        print(f'O {self.marca} {self.modelo} está freando.')


class Moto(Veiculo):
    def acelerar(self):
        print(f'A {self.marca} {self.modelo} está acelerando.')


    def frear(self):
        print(f'A {self.marca} {self.modelo} está freando.')


class Aviao(Veiculo):
    def acelerar(self):
        print(f'O {self.marca} {self.modelo} está acelerando.')
        

    def frear(self):
        print(f'O {self.marca} {self.modelo} está freando.')


    def decolar(self):
        print(f'O {self.marca} {self.modelo} está decolando.')


lista_veiculos = [Carro('Porsche', '911 Turbo S'), Moto('Honda', 'CBR 1000RR Fireblade'), Aviao('Embraer', 'KC390 Millenium')]

for item in lista_veiculos:
    item.acelerar()
    item.frear()
    
    if isinstance(item, Aviao):
        item.decolar()
    
    print('---')