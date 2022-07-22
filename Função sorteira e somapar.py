from random import randint
from time import sleep
def sorteia(lista):
    print('Somando os valores..')
    for c in range(0,5):
        n=randint(0,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.4)
    print('Acabou!')

números=list()
sorteia(números)

def somaPar(lista):
    s=0
    for valor in lista:
        if valor%2==0:
           s=s+valor
    print(f'A soma dos números pares na lista {lista} é de {s}')

somaPar(números)
 