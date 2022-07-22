from logging import exception
from uteis import binário
try:
    núm=int(input('Digite um número inteiro: '))
except ValueError:
    print('\033[31mOcorreu um erro! Tipos de valores não compatíveis :(')
except KeyboardInterrupt:
    print('\033[31mOcorreu um erro, o usuário preferiu não digitar nada :(')
except NameError:
    print('\033[31mOcorreu um erro, o seu programa tem um objeto não inicializado :(')
else:
    b=binário(núm)
    print(b)
finally:
    print('\033[mMuito obrigado, volte sempre!')

