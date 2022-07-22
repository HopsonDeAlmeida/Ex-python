l=[]
maior=0
menor=0
for c in range(0,5):
  l.append(int(input(f'Digite um valor na posição {c}: ')))
  if c==0:
      maior=menor=l[c]
  else:
      if l[c]>maior:
          maior=l[c]
      if l[c]<menor:
         menor=l[c]
print(f'O maior número digitado é {maior} na posição (ções) ', end='')
for i, v in enumerate(l):
    if v==maior:
        print(f'{v}...', end='')
print(f'\nO menor número digitado é {menor} na posição (ções) ', end='')
for i, v in enumerate(l):
    if v==menor:
        print(f'{v}...', end='')
