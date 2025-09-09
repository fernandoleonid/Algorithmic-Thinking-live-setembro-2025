aluno = input("Digite seu nome: ")
nota1 = int(input("Digite sua nota 1: "))
nota2 = int(input("Digite sua nota 2: "))

media = (nota1 + nota2) / 2

if media >= 5:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print (f"{aluno} tem média {media} e está {situacao}")