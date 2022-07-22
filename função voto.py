def voto(idade):
    if idade > 17 and idade < 65:
        return op1
    elif idade > 65:
        return op2
    else:
        return op3
    


ano=int(input('Em que você nasceu?: '))
ano_a=2022
idade= ano_a - ano
op1="VOTO é OBRIGATÓRIO"
op2="VOTO é OPCIONAL"
op3="NÃO VOTA"
print(f'Com a idade de {idade} anos, {voto(idade)}')