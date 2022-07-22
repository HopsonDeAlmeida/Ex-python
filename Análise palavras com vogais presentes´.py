pl=list()
pl.append(input(str('Digite alguma palavra: ')))
for p in pl:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aàáãâeiou':
            print(letras, end=' ')