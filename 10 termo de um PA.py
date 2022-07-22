
p=int(input('Primeiro termo: '))
r=int(input('Razão: '))
décimo=p+(10-1)*r
for c in range(p,décimo+r,r):
     print(f'{c}', end=' -> ')
print('ACABOU')