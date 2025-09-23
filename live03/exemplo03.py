import os

bancoDados = [
    {
        "nome": "Fernando Leonid",
        "n1": "10",
        "n2": "2",
        "n3": "8"
    }
]

def limpar_tela():
    os.system('cls')

def pausar():
    input("Aperte ENTER para continuar...")

def menu():
    limpar_tela()
    print ("1 - Mostrar nome do Aluno")
    print ("2 - Mostrar a nota do Aluno")
    print ("3 - Mostrar a situação do Aluno")
    print ("0 - SAIR")

def mostrar_nome():
    nome = bancoDados[0]['nome']
    print (nome)


def calcular_nota():
    n1 = int(bancoDados[0]['n1'])
    n2 = int(bancoDados[0]['n2'])
    n3 = int(bancoDados[0]['n3'])
    nota = (n1 + n2 + n3) / 3
    return nota

def mostrar_nota():
    nota = calcular_nota()
    print (f"A nota do aluno é: {nota:.2f}")

def mostrar_situacao():
    nota = calcular_nota()
    if (nota >= 5):
        print ("Aprovado")
    else:
        print ("Reprovado")


resposta =  -1
while resposta != 0:
    menu()
    resposta = int(input ("Digite um opção: "))
    if ( resposta == 1 ):
        limpar_tela()
        mostrar_nome()
        pausar()
    elif ( resposta == 2 ):
        limpar_tela()
        mostrar_nota()
        pausar()
    elif ( resposta == 3 ):
        limpar_tela()
        mostrar_situacao()
        pausar()
    elif ( resposta == 0 ):
        print ("Saindo do sistema...")
    else:
        print ("Opção inválida!!!")
