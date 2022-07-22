from random import randint

jogadores={'jogador1': 'jogador1','jogador2':'jogador2','jogador3':'jogador3'}
Sor1=randint(1,10)
Sor2=randint(1,10)
Sor3=randint(1,10)
print(f'{jogadores["jogador1"]} sorteou: {Sor1}')
print(f'{jogadores["jogador2"]} sorteou: {Sor2}')
print(f'{jogadores["jogador3"]} sorteou: {Sor3}')
maior=jogadores["jogador1"]
if Sor2 > Sor1 and Sor2 > Sor3:
    maior=jogadores["jogador2"]
if Sor3 > Sor1 and Sor3 > Sor2:
    maior=jogadores["jogador3"]
print(f'O (s) Vencedor (res) é (são) {maior}')

