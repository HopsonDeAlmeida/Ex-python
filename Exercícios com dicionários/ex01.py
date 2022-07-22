aluno=dict()
dados=list()
for c in range(0,1):
    aluno['Nome'] = str(input('Nome: '))
    aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
    if aluno['Média'] >= 10.0 and aluno['Média'] <= 20:
        print(f'O {aluno["Nome"]} teve {aluno["Média"]} e aprovou')
    elif aluno['Média'] > 20:
        print('Nota inválida...')
    else:
        print(f'O {aluno["Nome"]} teve {aluno["Média"]} e reprovou')
    