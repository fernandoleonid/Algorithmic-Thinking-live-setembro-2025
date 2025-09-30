from manipulador_arquivos import *


def escolher (opcao):
    if opcao == "1":
        tarefa = input ('Digite a nova tarefa: ')
        escrever_arquivo (tarefa)
    elif opcao == "2":
        tarefas = ler_arquivo()
        print (tarefas)
    elif opcao == "3":
        print ('Excluindo tarefas...')
        limpar_arquivo()
    elif opcao == "0":
        print ('Saindo do Sistema...')
        exit ()
    else:
        print ('Opção inválida!')


def exibir_menu ():
    print ('---> MENU <---')
    print ('1 - Adicionar tarefa')
    print ('2 - Listar tarefas')
    print ('3 - Excluir tarefas')
    print ('0 - Sair')
    opcao = input ('Digite uma opção: ')
    escolher (opcao)

    exibir_menu()


exibir_menu()