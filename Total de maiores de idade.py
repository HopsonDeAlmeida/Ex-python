totm=0
totmn=0
for c in range(1,7+1):
    idade=int(input(f'Digite a idade da {c}º pessoa: '))
    if idade>=18:
        totm+=1
    else:
        totmn+=1
print(f'O total de maiores de idade é de {totm} pessoas')
print(f'O total de menores de idade é de {totmn} pessoas')
    
