# Fatorial
n = int(input('Número: '))


f = 1
while n > 0:
    f*=n
    print(n,end='')
    print(' x ' if n>1 else ' = ', end='')
    n-=1
print(f)
