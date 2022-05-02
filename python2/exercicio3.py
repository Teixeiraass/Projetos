valor = float(input("Valor da compra: "))

if valor > 200:
  desconto = valor * 20 / 100
  total = valor - desconto
  print(total)
else:
  print(valor)