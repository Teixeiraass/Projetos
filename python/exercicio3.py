anos = int(input("Quantos anos: "))
meses = int(input("Quantos meses: "))
dias = int(input("Quantos dias: "))

calAnos = 365 * anos
calMeses = 30 * meses

idade = calAnos + calMeses + dias

print("Sua idade em dias é: ", idade)