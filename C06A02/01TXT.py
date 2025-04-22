import os

texto = 'Cientista de Dados pode ser uma excelente alternativa de carreira.\n'
texto += 'Esses profissionais precisam saber como programar em Python.\n'
texto += 'E, claro, devem ser proficientes em Data Science.'

os.makedirs('C06A02/arquivos', exist_ok=True)
arquivo = open(os.path.join('C06A02/arquivos/cientista.txt'), 'w')

for palavra in texto.split():
    arquivo.write(palavra + ' ')

arquivo.close()

#arquivo = open('C06A02/arquivos/cientista.txt', 'r')
#conteudo = arquivo.read()
#arquivo.close()
#print(conteudo)

with open('C06A02/arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))
print(conteudo)

with open('C06A02/arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write((texto[:19]))
    arquivo.write('\n')
    arquivo.write(texto[28:66])

with open('C06A02/arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)