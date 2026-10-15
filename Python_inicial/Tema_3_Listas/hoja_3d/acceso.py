"""'
Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son
correctos y permita el acceso solo si ambos son correctos.
"""

# --- lista usuarios ---
userList = [["juan123", "clave123"], ["ana456", "clave456"], ["pedro789", "clave789"]]

# --- pedir usuario y contraseña ---
name = input("Nombre de usuario: ")
password = input("Contraseña: ")

# --- comprobar acceso ---
if [name, password] in userList:
    print(f"Bienvenido {name}!!")
else:
    print("Credenciales inválidas!!")
