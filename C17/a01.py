import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

(imagens_treino, labels_treino), (imagens_teste, labels_teste) = datasets.cifar10.load_data()
nomes_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

imagens_treino = imagens_treino / 255.0
imagens_teste = imagens_teste / 255.0

def visualiza_imagens(images, labels):
    plt.figure(figsize = (10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap = plt.cm.binary)
        plt.xlabel(nomes_classes[labels[i][0]])
    plt.show()


visualiza_imagens(imagens_treino, labels_treino)

modelo_dsa = models.Sequential()

modelo_dsa.add(layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (32, 32, 3)))
modelo_dsa.add(layers.MaxPooling2D((2, 2)))

modelo_dsa.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
modelo_dsa.add(layers.MaxPooling2D((2, 2)))

modelo_dsa.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
modelo_dsa.add(layers.MaxPooling2D((2, 2)))

modelo_dsa.add(layers.Flatten())
modelo_dsa.add(layers.Dense(64, activation = 'relu'))
modelo_dsa.add(layers.Dense(10, activation = 'softmax'))

print(modelo_dsa.summary())

modelo_dsa.compile(optimizer = 'adam',
                   loss = 'sparse_categorical_crossentropy',
                   metrics = ['accuracy'])

history = modelo_dsa.fit(imagens_treino,
                         labels_treino,
                         epochs = 10,
                         validation_data = (imagens_teste, labels_teste))

erro_teste, acc_teste = modelo_dsa.evaluate(imagens_teste, labels_teste, verbose = 2)
print(f'\nAcurácia com Dados de Teste: {acc_teste}.')

nova_imagem = Image.open('C17/dados/nova_imagem.jpg')
print(nova_imagem.size)

largura = nova_imagem.width
altura = nova_imagem.height
print(f'A largura da imagem é: {largura}.')
print(f'A altura da imagem é: {altura}.')

nova_imagem = nova_imagem.resize((32, 32))

plt.figure(figsize = (1, 1))
plt.imshow(nova_imagem)
plt.xticks([])
plt.yticks([])
plt.show()

nova_imagem_array = np.array(nova_imagem) / 255.0
nova_imagem_array = np.expand_dims(nova_imagem_array, axis = 0)

previsoes = modelo_dsa.predict(nova_imagem_array)
print(previsoes)

classe_prevista = np.argmax(previsoes)
nome_classe_prevista = nomes_classes[classe_prevista]
print(f'A nova imagem foi classificada como: {nome_classe_prevista}.')