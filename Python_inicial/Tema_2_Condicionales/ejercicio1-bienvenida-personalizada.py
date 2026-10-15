texto = "Hola, "
print("¿Cómo te llamas?")
nombre = input()
nombre = nombre.replace(".", "").title()
nombre = nombre.replace("#", "").title()
if nombre == "Alejandro":
    print("!Hola, Alejandro!")
elif nombre == "Sergio":
    print("!Hola, Sergio!")
elif nombre == "Naomi":
    print("!Hola, Naomi!")
else:
    print("!Hola invitado!")
