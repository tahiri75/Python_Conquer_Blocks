numero = int(input("Teclee el número: "))
potencia = int(input("Teclee la potencia: "))

resultado = numero**potencia

if resultado % 2 == 0:
    print("numero ^ potencia = ", resultado, " es par")
else:
    print("numero ^ potencia = ", resultado, " es impar")
