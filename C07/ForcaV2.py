import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_hangman(chances):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
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
                   |      |
                   |      |
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
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]


def game():
    limpa_tela()
    print('z\nBem-vindo(a) ao Jogo da Forca!')
    print('Adivinhe a palavra abaixo:\n')

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'pessego', 'manga', 'maça', 'abacaxi']
    palavra = random.choice(palavras).upper()
    lista_letras_palavras = [letra for letra in palavra]
    tabuleiro = ['_'] * len(palavra)
    chances = 6
    letras_tentativas = []

    while chances > 0:
        print(display_hangman(chances))
        print(f'Palavra: {tabuleiro}.')
        print('\n')

        tentativa = input('\nDigite uma letra: ').upper()

        if tentativa in letras_tentativas:
            print('Você já tentou essa letra. Escolha outra!')
            continue
        
        letras_tentativas.append(tentativa) 
        
        if tentativa in lista_letras_palavras:
            print('Você acertou a letra!')
            
            for indice in range(len(lista_letras_palavras)):
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
            
            if '_' not in tabuleiro:
                print(f'Você venceu! A palavra era {palavra}!')
                break
        else:
            print('Essa letra não está na palavra!')
            chances -= 1
    
    if '_' in tabuleiro:
        print(f'Você perdeu, a palavra era: {palavra}.')


if __name__ == "__main__":
    game()
    print('\nParabéns. Você está aprendendo programação em Python com a DSA.\n')