import csv

# Criação de arquivo CSV:
with open('C06A02/arquivos/numeros.csv', 'w', newline='') as arquivo:
    # Cria o objeto de gravação:
    writer = csv.writer(arquivo)

    # Grava no arquivo linha a linha:
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63,87,92))
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

# Leitura de arquivo CSV:
with open('C06A02/arquivos/numeros.csv', 'r', encoding='utf8', newline= '\r\n') as arquivo:
    # Cria o objeto de leitura:
    leitor = csv.reader(arquivo)

    # Loop de leitura:
    for x in leitor:
        print(x)

# Passando os dados do arquivo CSV para variável:
with open('C06A02/arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)

# Imprimindo os dados armazenados na variável, excluindo o cabeçalho:
for linha in dados[1:]:
    print(linha)