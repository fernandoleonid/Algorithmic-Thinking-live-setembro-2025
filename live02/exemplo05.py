valores = [300, 400, 2340, 500, 100, 50, 1000]

def desconto_10 (valor):
    valor_novo = valor * 0.9
    return valor_novo

def verificar_maior_400(valor):
    return valor >= 400

valores_desconto = list(map(desconto_10, valores))

print (valores_desconto)

valores_maiores_400 = list(filter(verificar_maior_400, valores))

print (valores_maiores_400)