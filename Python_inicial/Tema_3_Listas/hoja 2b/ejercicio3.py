print("Teclee las longitudes de los 3 lados: ")
x = int(input())
y = int(input())
z = int(input())

# --- comprobar si puede ser un triangulo ---
if (x + y > z) and (y + z > x) and (x + z > y):
    print("se puede construir un triángulo con esos lados ")
else:
    print("No se puede construir un triángulo con esos lados")
