produtos = [
    {
        "nome": "teclado",
        "preco": 100.99,
        "cor": "Azul"
    }, 
    {
        "nome": "mouse",
        "preco": 99.99,
        "cor": "Preto"
    }, 
    {
        "nome": "Monitor",
        "preco": 1099.99,
        "cor": "Branco"
    }
]

def desconto_10 (produto):
    valor_novo = produto["preco"] * 0.9
    produto["preco"] = valor_novo
    return produto

produtos_desconto = list(map(desconto_10, produtos))

print (produtos_desconto)