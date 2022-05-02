h = float(input("Tronco da piramide: "))
Bmenor = float(input("Base menor: "))
Bmaior = float(input("Base maior: "))

volume = h/3 * (Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2) **0.5)

print(volume)