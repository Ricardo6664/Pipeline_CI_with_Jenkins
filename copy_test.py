lista = {}
def adic_lista():
    while True:
        nome_tarefa = input('\nDigite a tarefa: ')
        lista[nome_tarefa] = input("Coloque a descrição e data de vencimento: ")
        conti = input("Continuar [s]/[n]? ")
        if conti == 'n':
            break
def task_check():
    while True:
        task = input('\nDigite a tarefa a ser concluida: ')
        print("A tarefa escolhida é: ",lista[task])
        lista[task] =  'concluido'
        print(lista)
        conti = input("Continuar [s]/[n]? ")
        if conti == 'n':
                break
def edit_task():
    while True:
        escolha_edit = int(input('Escolha o que voce quer editar: [1]Titulo // [2]Data ou descrição: '))
        if escolha_edit == 1:
            task_edit = input("Qual titulo quer editar: ")
            #for titulo, _ in lista.items():
            novo_titulo = input('Digite novo titulo: ')
            lista[novo_titulo] = lista[task_edit]
            del lista[task_edit]
            print(lista)
            conti = input("Continuar [s]/[n]? ")
            if conti == 'n':
                break
        elif escolha_edit == 2:
            task_edit_descricao= input("\nDigite a tarefa a ser editada: ")
            print("A descrição da tarefa escolhida é: ",lista[task_edit_descricao])
            lista[task_edit_descricao] = input("Edite a nova descrição ou a nova data: ")
            print(lista)
            conti = input("Continuar [s]/[n]? ")
            if conti == 'n':
                break
def del_task():
    while True:
        exluir_tarefa = input('Digite a tarefa que voce quer exluir: ')
        if exluir_tarefa in lista.keys():
            lista.pop(exluir_tarefa)
            print(lista)
            conti = input("Continuar [s]/[n]? ")
            if conti == 'n':
                break

while True:
    print('Digite [1] para adicionar,[2] para concluir tarefa, [3] Editar tarefa, [4] Exclua a tarefa, [5] Visualizar a lista e [6]Finalizar programa')
    menu = int(input('Digite o Nº: '))
    if menu not in [1,2,3,4,5,6]:
        print("\nParabéns, quebrou o sistema")
        break
            
    
    if menu == 1:
        adic_lista()
        print('\nSe encontra pendente:\n Tarefas:',lista,'\n')
    elif menu == 2:
        task_check()
        print('\nTarefas totais:\n Tarefas:',lista,'\n')
    elif menu == 3:
        edit_task()
        print('\nEdite a tarefa:\n Tarefas:',lista,'\n')
    elif menu == 4:
        del_task()
        print('\Exclua a tarefa:\n Tarefas:',lista,'\n')
    elif menu == 5:
        print(lista)
    elif menu == 6:
        print("O programa está sendo finalizado...")
        i = 3
        while i != 0:
            print(i)
            i -= 1  
        print('Finalizado!')
        break  