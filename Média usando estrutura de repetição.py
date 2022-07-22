s=0
for c in range(1,4):
    n=int(input(f'Digite a {c}ª nota: '))
    s=s+n
    m=s/3
print(f'A média do aluno foi de {m}')
print('-='*20)
if m>=10 and m<15:
    print('O aluno foi aprovado')
if m>=15:
    
    print('O aluno foi aprovado com uma excelente nota, continua assim!')
if m>=9.5 and m<10:
    print('O aluno ainda pode ir a recurso')
if m<9.5:
    print('O aluno foi reprovado')
