from random import randint
from time import sleep

n = str(input('Aluno: '))
prof = randint(0,20)
print('Aguarde um momento...')
sleep(2)
print('A processar (Faltam 5 segundos)')
sleep(5)
print(f'A nota do {n} é de {prof} valores')
if prof >=10:
    print(f'{n} foi aprovado (a)')
else:
    print(f'{n} foi reprovado (a)')
