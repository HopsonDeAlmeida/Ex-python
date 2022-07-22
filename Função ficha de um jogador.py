
def fichajogador():
    print('-'*40)
    nome=""
    nome=str(input('Nome do jogador: ')).strip()
    g=str(input('Número de gols: ')).strip()
    if nome=="":
        nome="<desconhecido>"
    if g=='':
        g='0'
        g=int(g)
    g=int(g)
    print(f'O jogador {nome} fez {g} gol(s) no campeonato')
fichajogador()
