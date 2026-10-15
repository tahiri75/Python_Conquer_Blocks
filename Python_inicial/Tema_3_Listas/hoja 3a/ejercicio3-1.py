# --- pedir el numero ---
numero = int(input("Ingrese un numero: "))

# --- imprimir * hasta el numero ---
for i in range(1, numero + 1):
    print("*" * i)

# --- imprimir * hasta el numero al reves ---
for i in range(numero - 1, 0, -1):
    print("*" * i)
