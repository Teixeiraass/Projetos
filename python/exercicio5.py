from cmath import tan
import math


graus = float(input("Valor em graus: "))

radianos = 3.14 * graus / 180

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print("Valor em radianos:",radianos)
print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)