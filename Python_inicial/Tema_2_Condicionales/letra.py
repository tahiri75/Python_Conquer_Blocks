# --- entrar la letra ---
letra = input("teclee una letra: ")

# --- comprobar si es una letra ---
if len(letra) > 1:
    print("No es una letra")
# --- comprobar si es mayuscula ---
elif letra == letra.upper():
    print("mayúscula")
# --- comprobar si es minuscula ---
elif letra == letra.lower():
    print("minúscula")
