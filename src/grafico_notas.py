# plt é o alias padrão adotado pela comunidade Python para o módulo pyplot.
import matplotlib.pyplot as plt
import random

# Quantidade de provas: 8
x = list(range(1,9))

#
# Gera 8 notas aletários com valores entre 0 e 10
#
y = []
for nota in range(0,8):
    y.append(random.randrange(0,11))

# marker define o caracter que aparecerá no ponto de interseção dos eixos x e y
plt.plot(x,y, marker='o')
plt.title('Notas de Matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
# Aqui no PyCharm o gráfico não é exibido enquanto o método show() não for executado.
plt.show()