import re

# Variável do tipo string:
musica = '''
Todos os dias quando acordo
Não tenho mais o tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo que esse sangue amargo
E tão sério
E selvagem!
Selvagem!
Selvagem!
Veja o sol dessa manhã tão cinza
A tempestade que chega é da cor dos teus olhos
Castanhos
Então me abraça forte!
Me diz mais uma vez que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas
Agora
O que foi escondido é o que se escondeu
E o que foi prometido, ninguém prometeu
Nem foi tempo perdido
Somos tão jovens!
Tão jovens!
Tão jovens!
'''

print(musica)
print('=' * 50)

ocorrencias = re.findall(r'a', musica)
print(f'O caracter "a" aparece {len(ocorrencias)} vezes.')

ocorrencias2 = re.findall(r'\btempo\b', musica)
print(f'A palavra "tempo" aparece {(len(ocorrencias2))} vezes.')

exclamadas = re.findall(r'\b\w+!', musica)
print(f'Palavras seguidas por exclamação: {exclamadas}.')

resultado = re.findall(r'\besse (\w+) amargo\b', musica)
print(f'Palavras antecedidas por "esse" e sucedidas por "amargo": {resultado}.')

resultado2 = re.findall(r'(\w)([áéíóúàèìòùâêîôûãõ])', musica, re.IGNORECASE)
pre_acento = [match[0] for match in resultado2]
print(f'Letras que antecedem letras acentuadas: {pre_acento}.')