n = (int(input('Digite um valor:')),
int(input('Digite um valor:')),
int(input('Digite um valor:')),
int(input('Digite um valor:')))

print(f'Digitaste os seguintes valores {n} ')
print(f'O maior número é {max(n)}')
if 4 in n:
    print(f'O número 4 está repetido {n.count(4)} vez(s)')
else:
    print('O número 4 não foi digitado')
if 7 in n:
    print(f'O número 7 está na {n.index(7)+1}ª posição')
else:
    print('O número 7 não foi digitado..')
print('Os números pares digitados foram: ', end=' ')
for c in n:
    if c%2==0:
        print(f'({c}',end='..)')