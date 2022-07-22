


def fatorial(n):
    f=1
    for c in range(n,0,-1):
        print(c, end='')
        f*=c
        print(' x ' if c>1 else ' = ', end=' ')
    print(f, end='')
def dobro(n):
    n=n*2
    return n
def triplo():
    n=n*3
    return n
def binário(n):
    valores=""
    inverso=""
    if n==2:
      inverso="0010"
    elif n==4:
       inverso="0100"
    elif n==8:
       inverso="1000"
#-----------------------------------------
# Para converter qualquer número---------
    else:
        while n>2:
            m=int
            m=n%2
            m=int(m)
            m=str(m)
            valores+=m
            n/=2  
        if n<2:
            valores+='1'
        li=valores.split()
        li="".join(li)
        inverso=li[::-1]
    '''for números in range(len(li)-1,-1):
        inverso+=li[números]'''
#--------------------------------------------------------
# Para números menores que 10.
    if len(inverso)==2:
        li+='00'
        inverso=li[::-1]
    if len(inverso)==3:
        li+='0'
        inverso=li[::-1]
    if len(inverso)==1:
        li+='000'
        inverso=li[::-1]
#-----------------------------------------------
# Para o número 0.

    if n==0:
        inverso="0000"
#-----------------------------------------------

    print(inverso)
def antecessor():
    n=n-1
    return n
def sucessor():
    n=n+1
    return n
def escreva(text):
    text=str(text)
    print(text)
escreva('Olá mundo')

