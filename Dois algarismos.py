n = str(input('Digite dois algarismos: '))
inter=int(n)
#-------------------ERRO------------------
if inter <= 10 or inter >= 100:
    print('Tente mais uma vez....')
    n = str(input('Digite dois algarismos: '))
#--------------------ERRO-----------------
print(f'O primeiro valor é {n[0]} e o segundo número é {n[1]}')
n1=int(n[0])
n2=int(n[1])
s = n1 + n2
print(f'A soma é de {s} ')

