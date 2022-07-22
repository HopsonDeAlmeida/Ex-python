v = int(input('Digite a velocidade do veículo: '))
if v == 80:
    multa=1000
    print(f'Foste multado(a), pagarás {multa}kzs')
if v>80:
    multa=(v-80)*1000
    print(f'Passou o limite da velocidade autorizada, pagarás a multa de {multa}kz')


        

