import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


board = [ """
         --------- FORCA ---------

                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """]

class Hangman:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []


    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False    
        return True
    

    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)
    

    def hangman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False
    

    def hide_palavra(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    

    def print_game_status(self):
        print(board[len(self.letras_erradas)])
        print(f'\nPalavra: {self.hide_palavra()}')
        print(f'\nLetras erradas: ',)

        for letra in self.letras_erradas:
            print(letra,)
        
        print()
        print('Letras corretas: ',)
        
        for letra in self.letras_escolhidas:
            print(letra,)
        
        print()


def rand_palavra():
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'pessego', 'manga', 'maca', 'abacaxi']
    palavra = random.choice(palavras)
    return palavra


def main():
    limpa_tela()
    
    game = Hangman(rand_palavra())

    while not game.hangman_over():
        game.print_game_status()
        user_input = input('Digite uma letra: ')
        game.guess(user_input)

    game.print_game_status()

    if game.hangman_won():
        print(f'\nParabéns, você venceu!\nA palavra é: {game.palavra.upper()}.')
    else:
        print(f'\nGame Over! A palavra era: {game.palavra.upper()}.')
    
    print('\nObrigado por jogar!')


if __name__ == '__main__':
    main()