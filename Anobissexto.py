print('=-'*5,'ANO BISSEXTO','=-'*5)
ano = int(input('Digite o ano: '))
if ano % 4 ==0 and ano%100!=0 or ano%400==0:
    print(f'O ano "{ano}" é um ano BISSEXTO')
else:
    print(f'O ano "{ano}" não é um ano BISSEXTO')