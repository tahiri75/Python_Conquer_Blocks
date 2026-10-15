# --- ENCRIPTACIÓN ROT13 ---

alfabeto = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

frase = input("Escriba la frase que desea encriptar: ")

fraseEncriptada = ""

nuevoCaracter = ""

for caracter in frase:
    if caracter.lower() in alfabeto:
        pos = alfabeto.index(caracter.lower())
        nuevaPos = pos + 13
        if nuevaPos > 25:
            nuevaPos = nuevaPos - 26
        nuevoCaracter = alfabeto[nuevaPos]
        if caracter.isupper():
            nuevoCaracter = nuevoCaracter.upper()
    else:
        nuevoCaracter = caracter
    fraseEncriptada = fraseEncriptada + nuevoCaracter

print("La frase encriptada es: ", fraseEncriptada)
