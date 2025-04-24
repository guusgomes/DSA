import re

texto = 'Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com.'

# Expressão regular para contar quantas vezes o caracter arroba aparece no texto:
resultado = len(re.findall('@', texto))
print(f'O caractere "@" apareceu {resultado} vezes no texto.')

# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto:
resultado2 = re.findall(r'você (\w+)', texto)
print(f'A palavra aprós "você" é: {resultado2[0]}.')

# Expressão regular para extrair endereços de e-mail de uma string:
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
cont = 0

for e in emails:
    print(emails[cont])
    cont += 1

text = 'O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender.'

# Extraindo os advérbios da frase:
for m in re.finditer(r'\w+mente\b', text):
    print(f'{m.start()} - {m.end()}: {m.group(0)}')