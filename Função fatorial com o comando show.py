def fatorial(número,show=False):
    f=1
    print('-'*40)
    # Use o comando show para exibir o processo do cálculo do fatorial
    for c in range(número,0,-1):
            f*=número
            if show == True:
                print(número, end=' ')
                print(' x ' if número > 1 else ' = ', end='')
            número-=1
    print(f)

        
        



      