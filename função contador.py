from time import sleep
def linha():
    print('~'*30)
def contador():
    inicio=int(input('Ínicio: '))
    fim=int(input('Fim: '))
    pulo=int(input('Pulos: '))
    if pulo==0:
        pulo=1
    print('~'*30)
    print(f'Contagem de {inicio} à {fim} pulando de {pulo} em {pulo}')
    if inicio > fim:
        if pulo<0:
            pulo=pulo
        else:
            pulo=-(pulo)
    fim=fim+pulo
    if inicio==1:
        fim=fim-1
    for c in range(inicio,fim, pulo):
        sleep(0.3)
        print(c, end=' ')   
print('FIM')
print()
linha()
print('Contagem de 1 até 10 de 1 em 1')
for p in range(1,10+1):
    sleep(0.3)
    print(F'{p}',end=' ')
print(' FIM!')
print()
linha()
print('Contagem de 10 até 0 de 2 em 2')
for r in range(10,-1,-2):
    sleep(0.3)
    print(r, end='  ')
print(' FIM!')
print()
linha()
print('Agora é sua vez de personalizar a contagem')
contador()
print()
linha()


