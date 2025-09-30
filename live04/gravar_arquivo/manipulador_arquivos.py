def escrever_arquivo (texto):
    arquivo = open ('banco_dados.txt', 'a')
    arquivo.write(texto + '\n')
    arquivo.close()

def ler_arquivo ():
    arquivo = open('banco_dados.txt')
    conteudo = arquivo.read()
    arquivo.close
    return conteudo

def limpar_arquivo ():
    arquivo= open ('banco_dados.txt', 'w')
    arquivo.write('')
    arquivo.close