class Animal():
    def __init__(self):
        print('Animal criado.')
    

    def imprimir(self):
        print('Este é um animal.')


    def comer(self):
        print('Hora de comer.')
    

    def emitir_som(self):
        pass


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto Cachorro criado.')


    def emitir_som(self):
        print('AU! AU!')


class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto Gato criado.')


    def emitir_som(self):
        print('MIAU!')


rex = Cachorro()
zeze = Gato()

rex.emitir_som()
zeze.emitir_som()
rex.imprimir()
rex.comer()
zeze.comer()