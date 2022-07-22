from time import sleep

n=int(input('Digite um valor: '))
n1=int(input('Digite um valor: '))
menu=0
while menu!=5:
    print('-'*20)
    print('''    [1] Soma
    [2] Multiplicar
    [3] Maior número
    [4] novos valores
    [5] Sair do programa''')
    menu=int(input('Digite o menu representado por número: '))
    if menu==1:
        s=n+n1
        print(f'Soma: {n} + {n1} = {s}')
    if menu==2:
       m=n*n1
       print(f'Multiplicação: {n} x {n1} = {m}') 
    if menu==3:
        if n>n1:
            print(f'Maior número: {n}')
        if n1>n:
            print(f'Maior número: {n1}')
    if menu==4:
        print('Digite novos valores...')
        print('-'*40)
        n=int(input('Digite um valor: '))
        n1=int(input('Digite um valor: '))
print('Processando....')
sleep(2)
