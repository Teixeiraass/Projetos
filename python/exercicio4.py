valorPrestacao = float(input("Valor da prestação: "))
multa = 2 
dias = int(input("Quantidade de dias: "))

prestacao = valorPrestacao + (valorPrestacao * multa / 100 * dias)

print(prestacao)
