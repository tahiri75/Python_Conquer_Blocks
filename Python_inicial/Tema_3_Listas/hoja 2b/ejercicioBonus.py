letra = str(input("Teclee una letra: "))

# --- comprobar si es mayuscula o minuscula ---
if letra == letra.upper():
    print("La letra es mayúscula")
elif letra == letra.lower():
    print("La letra es minúscula")
else:
    print("no es una letra")
