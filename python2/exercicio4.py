salario = float(input("Digite seu salario: "))
luz = float(input("Valor da conta de luz: "))
agua = float(input("Valor da conta de água: "))
gaz = float(input("Valor da conta de gaz: "))

totalC = gaz + luz + agua

if salario < totalC:
  print("Salario insuficiente")
else: 
  resto = salario - totalC
  print(resto)