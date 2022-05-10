from time import sleep
import interface # vou importar a função "cabeçalho" e "lin" - modularização.

while True:
    # Listas onde irão ficar armazenados os nomes com a funções.
    pessoas_funçao = []
    princ = []
    # Título
    interface.cabeçalho('GERENCIADOR DE TAREFAS', '-', 50)
    # quantidade de pessoas que irão participar.
    quant = int(input('>>>> Quantas pessoas irão participar? '))
    interface.lin('-',50)
    # nome e função da pessoas.
    for cont in range(1, quant+1):
        pessoas_funçao.append(str(input(f'{cont}º Nome: ')).strip())
        pessoas_funçao.append(str(input(f'Qual será a função da {cont}º pessoa? ')).strip())
        princ.append(pessoas_funçao[:])
        pessoas_funçao.clear()
        interface.lin('-',50)
    print('CRIANDO LISTA...')
    sleep(2)
    interface.lin('-',50)
    # Lista com os nomes e funções.
    print('-'*20, ' LISTA ', '-'*21)
    print(f'{"No":<4}{"NOMES":<15}{"FUNÇÕES"}')
    for posi, pf in enumerate(princ):
        print(f'{posi:<4}{pf[0]:<15}{pf[1]}')
    interface.lin('-',50)
    break

while True:
    # opção de adicionar mais pessoas a lista.
    opçao = ' '
    while opçao not in 'SN':
        opçao = str(input('>>>> Deseja adicionar mais pessoas? [S/N] ')).upper()[0]
    print('CARREGANDO....')
    sleep(1)
    interface.lin('-',50)
    if opçao == 'S':
        # vai perguntar quantas pessoas irão ser adicionadas.
        adicionador = int(input('>>>> Quantas pessoas gostaria de adcionar? '))
        interface.lin('-',50)
        for cont in range(1,adicionador+1):
            pessoas_funçao.append(str(input(f'{cont}º Nome: ')).strip())
            pessoas_funçao.append(str(input(f'Qual será a função da {cont}º pessoa? ')).strip())
            princ.append(pessoas_funçao[:])
            pessoas_funçao.clear()
            interface.lin('-',50)
        print('ATUALIZANDO...')
        sleep(2)
        interface.lin('-',50)
        # irá mostrar a lista atualizada, com mais pessoas.
        print('-'*20, ' LISTA ', '-'*21)
        print(f'{"No":<4}{"NOMES":<15}{"FUNÇÕES"}')
        for posi, pf in enumerate(princ):
                print(f'{posi:<4}{pf[0]:<15}{pf[1]}')
        interface.lin('-',50)
    else:
        break

# para visualizar o nome e função da pessoa na lista.
while True:
    opc_seleção = ' '
    while opc_seleção not in 'SN':
        opc_seleção = str(input('>>>> Deseja visualizar a função de alguém? [S/N] ')).upper()[0]
    print('CARREGANDO....')
    sleep(1)
    interface.lin('-',50)
    if opc_seleção == 'S':
        # Opção de selecionar a pessoa e mostrar ela na lista.
        seleção = int(input('>>>> Quem da lista você deseja visualizar a função? (No) '))
        interface.lin('-',50)
        print('-' * 20, ' LISTA ', '-' * 21)
        print(f'{"No":<4}{"NOME":<15}{"FUNÇÃO"}')
        print(f'{seleção:<4}{princ[seleção][0]:<15}{princ[seleção][1]}')
        interface.lin('-',50)
    else:
        # vai finalizar o programa.
        sleep(1)
        print('<<< PROGRAMA FINALIZADO >>>')
        break
