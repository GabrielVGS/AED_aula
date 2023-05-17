peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
while altura <= 0:
	altura = float(input("Digite uma altura válida: "))
imc = peso/(altura**2)
print("{:.2f}".format(imc))
