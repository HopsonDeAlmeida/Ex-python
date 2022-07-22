somaid=0
médiaid=0
Homemmaisvelhoidade=0
nomedohomemmaisvelho=0
totmulhermenor20=0


for c in range(1,5):
    print(f'-------{c}ª PESSOA-------')
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('sexo[M/F]: ')).upper()
    somaid+=idade
    if c ==1 and sexo in 'Mm':
        Homemmaisvelhoidade=idade
        nomedohomemmaisvelho=nome
    if sexo in 'Mm' and idade > Homemmaisvelhoidade:
        Homemmaisvelhoidade=idade
        nomedohomemmaisvelho=nome
    if sexo in 'Ff' and idade < 20:
        totmulhermenor20+=1
    
médiaid=somaid/4

print(f'A média da idade é de {médiaid}')
print(f' O homem mais velho chama-se {nomedohomemmaisvelho} com a idade de {Homemmaisvelhoidade} anos')
print(f'Ao todo existem {totmulhermenor20} mulheres menores que 20 anos')
