from random import randint
cpu=randint(0,5)
n = int(input('Advinha um número de (0 à 5):  '))
if n == cpu:
    print('Você acertou!!')
else:
    print(f'Você errou, a resposta certa é {cpu}')