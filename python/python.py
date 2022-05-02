nome = input("Nome do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = nota1 + nota2 / 2

if media >= 6:
    print("O aluno:", nome, "esta aprovado")
else:
    print("O aluno:", nome, "esta reprovado")