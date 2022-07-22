pessoas=[]
dados=[]
tmaior=tmen=0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for m in pessoas:
    if m[1]>18:
        print(f'O {m[0]} maior de idade')
        tmaior+=1
    else:
        print(f' O {m[0]} é menor de idade')
        tmen+=1
print(f'O total de maiores de idade é {tmaior}')
print(f'O total de menores de idade é de {tmen}')
    