from random import randint

n= (randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10))

print('Os números sorteiados são: ',end='')
for nu in n:
    print(f'{nu}'+',', end='')
print(f'\n O maior número é {max(n)}')
print(f'O menor número é {min(n)}')