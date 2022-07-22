from random import randint
from time import sleep

nota1=randint(0,20)
nota2=randint(0,20)
nota3=randint(0,20)
nota4=randint(0,20)

quadrodehonra=dict()

for c in range(1,5):
    n = str(input(f'{c}º Aluno: '))
    if c==1:
        n1=n
        print('-'*20,'*')
        print(f'{n} A nota do {n} é de {nota1}')
        if nota1>=10:
                print(f'{n}  aprovou')
        else:
                print(f'{n}  reprovou')
        print('-'*20,'*')
    else:
        if c==2:
            n2=n
            print('-'*20,'*')
            print(f'{n} A nota do(a) {n} é de {nota2}')
            if nota2>=10:
                print(f'{n}  aprovou')
            else:
                print(f'{n}  reprovou')
            print('-'*20,'*')
        if c==3:
            n3=n
            print('-'*20,'*')
            print(f'A nota do(a) {n} é de {nota3}')
            if nota3>=10:
                print(f'{n} aprovou')
            else:
                print(f'{n} reprovou')
            print('-'*20,'*')
        if c==4:
            n4=n
            print('-'*20,'*')
            print(f'{n} A nota do(a) {n} é de {nota4}')
            if nota4>=10:
                print(f'{n}  aprovou')
            else:
                print(f'{n}  reprovou')
            print('-'*20,'*')
             
print()
#--------------- Definindo quadro de honra-----------------
print('-'*20,'QUADRO DE HONRA','-'*20)
if nota1>=15:
    aluno1=n1
    print('',aluno1,'|',nota1,' valores')
if nota2>=15:
    aluno2=n2
    print('',aluno2,'|',nota2,' valores')
if nota3>=15:
    aluno3=n3
    print('',aluno3,'|',nota3,' valores')
if nota4>=15:
    aluno4=n4
    print('',aluno4,'|',nota4,' valores')
print('-'*57)


