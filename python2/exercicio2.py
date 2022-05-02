turno = input("Digite seu turno. (N) para noite, (T) para tarde e (M) para manha: ")
horas = float(input("Digite a quantidade de horas: "))

if turno == "N" or turno == "n":
  totalN = horas * 45
  print(totalN)
elif turno == "M" or turno == "m":
  total = horas * 35
  print(total)
elif turno == "T" or turno == "t":
  total = horas * 35
  print(total)