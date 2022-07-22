frase=str(input('Digite uma frase: ')).strip().upper()
palavra=frase.split()
junto=''.join(palavra)
inverso=''
'''for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]'''
inverso=junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')