texto = "estás usando Python"
print("¿Cómo te llamas?")
nombre = input()
nombre = nombre.replace(".", "").title()
mensaje = "¡Hola, " + nombre + ", " + texto + "!"
print(mensaje.upper())
print(mensaje.lower())
print(mensaje.title())
print(mensaje)
