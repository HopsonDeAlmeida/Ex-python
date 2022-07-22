r1=int(input('1º segmento: '))
r2=int(input('2º segmento: '))
r3=int(input('3º segmento: '))
if r1 < r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os três segmentos podem formar um TRIÂNGULO')
else:
    print('Os segmentos inseridos não podem formar um TRIÂNGULO')