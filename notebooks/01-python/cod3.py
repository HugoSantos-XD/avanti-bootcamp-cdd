"Crie um programa que peça ao usuário para advinhar um número secreto entre 1 e 100." 
"O programa deve fornecer dicas se o palpite do usuário é maior ou menor que o numero secreto," 
"até que ele advinhe corretamente"

import random

num_secret = random.randint(1, 100)
n = 0

print('Estou pensando em um número entre 1 e 100. Você consegue adivinhar qual é?')

while n != num_secret:
    n = int(input('Digite seu palpite: '))

    if n < num_secret:
        print('Seu palpite é muito baixo. Tente novamente!')
    elif n > num_secret:
        print('Seu palpite é muito alto. Tente novamente')
    else:
        print('Congratulations! You guessed the secret number!')
print('OBG POR JOGAR')