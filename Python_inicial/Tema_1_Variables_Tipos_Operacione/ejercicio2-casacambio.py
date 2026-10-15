tasaCambio = float(input("Ingrese la tasa de cambio de euros a dólares: "))
print("Ingrese la cantidad de euros que desea convertir a dólares:")
euros = float(input())
dolares = euros * tasaCambio
print(f"{euros} euros son {dolares} dólares.")
tasaGestion = 10
tasaGestionDecimal = tasaGestion / 100
dolaresConGestion = dolares * (1 - tasaGestionDecimal)
print(
    f"Después de aplicar una tasa de gestión del {tasaGestion}%, la cantidad final en dólares es: {dolaresConGestion}."
)
print("Ingrese la cantidad de dólares que desea convertir a euros:")
dolares = float(input())
euros = dolares / tasaCambio
print(f"{dolares} dólares son {euros} euros.")
eurosConGestion = euros * (1 - tasaGestionDecimal)
print(
    f"Después de aplicar una tasa de gestión del {tasaGestion}%, la cantidad final en euros es: {eurosConGestion}."
)
