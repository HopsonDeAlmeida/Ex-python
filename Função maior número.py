def maior(*n):  
    tam=len(n)
    print('-='*35)
    print(f'Números digitados {n} , contém {tam} Digitos e o maior número é {max(n)}')
# Usar está função para comparar números, e verificar quantos números foram digitados e qual é o maior número entre eles--- 
#Basta chamar a função "maior()" e dentro de parentesis digitar os valores separando com vírgulas..
maior(123,567,2,6,9)