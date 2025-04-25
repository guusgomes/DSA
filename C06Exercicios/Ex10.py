# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras 
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'

import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

padrao = r'Data Science (\w+)'
resultado = re.search(padrao, texto)

if resultado:
    print(f'A palavra é: {resultado.group(1)}.')
else:
    print("Nenhuma correspondência encontrada.")