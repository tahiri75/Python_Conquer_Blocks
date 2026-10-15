# --- guardar contraseña ---
contraseña = input("Ingrese la contraseña: ")

contraseña_correcta = False

while not contraseña_correcta:
    # --- confirmar contraseña ---
    confirmar_contraseña = input("Confirme la contraseña: ")

    # --- verificar si las contraseñas coinciden ---
    if contraseña == confirmar_contraseña:
        print("Las contraseñas coinciden.")
        contraseña_correcta = True
    else:
        print("Las contraseñas no coinciden.")
