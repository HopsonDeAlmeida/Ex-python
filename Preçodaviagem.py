d = float(input('Qual é a distância da viagem?(km): '))
if d<=200:
    preço=d*30.72
else:
    preço=d*30.72
print(f'Viagem ({d}km), preço {preço:.2f}kzs')