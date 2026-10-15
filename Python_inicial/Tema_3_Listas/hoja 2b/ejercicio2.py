# --- pedir al usuario que introduzca 3 números ---
print("Teclee 3 números: ")
x = int(input())
y = int(input())
z = int(input())

# --- comprobar si alguno es la suma de los otros dos ---
if x + y == z:
    print("el tercer número es la suma de los otros dos")
elif y + z == x:
    print("el primer número es la suma de los otros dos")
elif x + z == y:
    print("el segundo número es la suma de los otros dos")
else:
    print("ninguno es la suma de los otros dos")
