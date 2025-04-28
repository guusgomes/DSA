import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def game():
    limpa_tela()
    print('z\nBem-vindo(a) ao Jogo da Forca!')
    print('Adivinhe a palavra abaixo:\n')

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'pêssego', 'manga', 'maçã', 'abacaxi']
    palavra = random.choice(palavras).upper()
    letras_descobertas = ['_' for letra in palavra]
    chances = len(palavra)
    letras_erradas = []

    while chances > 0:
        print(' '.join(letras_descobertas))
        print(f'\nChances restantes: {chances}.')
        print(f'Letras erradas: {letras_erradas}.')

        tentativa = input('\nDigite uma letra: ').upper()
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa) 
        
        if '_' not in letras_descobertas:
            print(f'\nVocê venceu, a palavra é: {palavra}.')
            break
    
    if '_' in letras_descobertas:
        print(f'Você perdeu, a palavra era: {palavra}.')


if __name__ == "__main__":
    game()
    print('\nParabéns. Você está aprendendo programação em Python com a DSA.\n')