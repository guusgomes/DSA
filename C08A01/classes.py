class Livro():
    def __init__(self):
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        
        print('Construtor chamado para criar um objeto desta classe.')


    def imprime(self):
        print(f'Foi criado o livro {self.titulo} com ISBN {self.isbn}.')
              

Livro1 = Livro()

print(type(Livro1))
print(Livro1.titulo)
Livro1.imprime()


class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        
        print('Construtor chamado para criar um objeto desta classe.')


    def imprime(self, titulo, isbn):
        print(f'Foi criado o livro {titulo} com ISBN {isbn}.')
              

Livro2 = Livro('O Poder do Hábito', 77886611)
print(Livro2.titulo)
Livro2.imprime('O Poder do Hábito', 77886611)


class Algoritmo():
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print('Construtor chamado para criar um objeto desta classe.')


algo1 = Algoritmo(tipo_algo = 'Random Forest')
algo2 = Algoritmo(tipo_algo = 'Deep Learning')
print(algo1.tipo)
print(algo2.tipo)