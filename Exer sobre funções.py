def média(a,b,c):
    m=(a+b+c)/3
    print(f'A média é de {m}')
def soma(a,b):
    s=a+b
    print(f'A soma entre A + B é de {s}')
def lin(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
def dobra(list):
    pos=0
    while pos<len(list):
        list[pos]*=2
        pos+=1
def somamais(*valor):
    s=0
    for num in valor:
        s+=num
    print(f'Somando os valores {valor} temos - {s}')
def contador(*valore):
    tam=len(valore)
    print(f'{valore} com {tam} números')
contador(1,2,3,4,5)
valores=[1,2,4,5,8,9]