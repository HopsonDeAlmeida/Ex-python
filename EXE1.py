from random import randint

tentativas=0
computador=randint(0,10)
jogador=int(input('Tente adivinhar um número entre (0 à 10): \033[32m'))

while jogador != computador:
    jogador=int(input('\033[mTente adivinhar um número entre (0 à 10): \033[32m'))
    tentativas+=1

if jogador==computador:
    print(f'O computador pensou ({computador})')
    print(f'Você conseguiu! Com {tentativas} tentativas sem êxito\033[m')
