class Circulo():
    pi = 3.14

    def __init__(self, raio = 5):
        self.raio = raio
    

    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    

    def setRaio(self, novo_raio):
        self.raio = novo_raio
    

    def getRaio(self):
        return self.raio
    

circ = Circulo()
print(circ.getRaio())

circ1 = Circulo(7)
print(f'O raio é: {circ1.getRaio()}.')
print(f'A área é: {circ1.area()}.')

circ.setRaio(3)
print(f'Novo raio é: {circ.getRaio()}.')