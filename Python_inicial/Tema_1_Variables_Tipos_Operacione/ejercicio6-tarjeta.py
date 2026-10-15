tarjeta = str(input("Teclee el número de la tarjeta: "))
for i in range(len(tarjeta) - 4):
    if tarjeta[i] != " ":
        print("*", end="")
    else:
        print(" ", end="")
print(tarjeta[len(tarjeta) - 4 : len(tarjeta)])
