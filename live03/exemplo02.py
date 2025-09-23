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

for produto in produtos:
    print (f"O produto {produto['nome']} da cor {produto['cor']} vale {produto['preco']}")