n = str(input('Digite dois algarismos: '))
inte=int(n)
#--------------------------------------------
if inte < 10 or inte > 99:
    print('Valor inválido')
    n = str(input('Digite dois algarismos: '))
#----------------------------------------------
n1=int(n[0])
n2=int(n[1])
s=n1+n2
print(f'A soma é de {s}')