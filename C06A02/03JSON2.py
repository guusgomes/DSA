import json

# Imprimindo um arquivo JSON copiado da internet:
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print('Título: ', dados['title'])
print('URL: ', dados['url'])
print('Duração ', dados['duration'])
print('Número de visualizações: ', dados['stats_number_of_plays'])

# Copiando o conteúdo de um arquivo para outro:

# Nome dos arquivos:
arquivo_fonte = 'C06A02/arquivos/dados.json'
arquivo_destino = 'C06A02/arquivos/dados.txt'

# Método 1:
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

# Método 2:
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

# Leitura do arquivo txt:

with open('C06A02/arquivos/dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)