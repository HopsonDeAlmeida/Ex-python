s=0
for c in range(1,500+1):
    if c%2!=0:
        print(c, end='\n')
        s=s+c
print(f'A soma é de {s}')
