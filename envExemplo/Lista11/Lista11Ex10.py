import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produtos = [Produto("Camisa", 50), Produto("Calça", 80), Produto("Tênis", 120)]

# Mapeando os nomes de produtos para índices
classes = {p.nome: i for i, p in enumerate(produtos)}

# Transformando os dados em um array numpy
x = np.array([[p.preco] for p in produtos])
y = np.array([classes[p.nome] for p in produtos])

# Convertendo rótulos de classe para one-hot encoding
num_classes = len(classes)
y_one_hot = keras.utils.to_categorical(y, num_classes)

# Criação do modelo de rede neural
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compilando o modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinamento do modelo
model.fit(x, y_one_hot, epochs=100, batch_size=1)

# Testando o modelo
preco = np.array([[70]])
resultado = model.predict(preco)
print(resultado)
