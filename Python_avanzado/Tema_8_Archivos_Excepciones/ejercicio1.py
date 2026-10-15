"""'SUMA Y VALUEERROR
Un problema común al solicitar una entrada numérica ocurre cuando las
personas ingresan texto en lugar de números. Cuando intentas convertir la
entrada a un entero (int), obtendrás un ValueError. Escribe un programa que
solicite dos números. Suma los números y muestra el resultado. Captura el
ValueError si alguno de los valores de entrada no es un número e imprime un
mensaje de error amigable. Prueba tu programa ingresando dos números y
luego ingresando texto en lugar de un número. Envuelve tu código del en un
bucle while para que el usuario pueda continuar ingresando números incluso
si comete un error ingresando texto en lugar de un número."""

# definir función que sume dos números
# def suma(numero1, numero2):
#    return numero1 + numero2

suma_numeros = lambda numero1, numero2: numero1 + numero2

continuar = True
while continuar:
    # pedir los números hasta que el usuario decida terminar
    numero1 = input("Tecle el primer número o t para terminar: ")
    if numero1.lower() == "t":
        print("Terminar")
        continuar = False
    else:
        numero2 = input("Tecle el segundo número o t para terminar: ")
        if numero2.lower() == "t":
            print("Terminar")
            continuar = False
        else:
            # sumar los números y capturar exception al convertir los números a int
            try:
                suma = suma_numeros(int(numero1), int(numero2))
                print("La suma es: ", suma)
            except ValueError:
                # mostrar error si alguno de los números es inválido
                print("Número inválido")
