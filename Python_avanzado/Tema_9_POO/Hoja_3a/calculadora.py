"""'CALCULADORA BÁSICA
Crea una clase llamada "Calculadora" con métodos para sumar, restar,
multiplicar y dividir. Crea objetos de esta clase y realiza algunas operaciones
básicas."""


# definición de la clase
class calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        return self.numero1 / self.numero2


continuar = True
while continuar:

    # pedir los números
    num1 = input("Teclee el primer número: ")
    num2 = input("Teclee el segundo número ")

    # try para capturar errores
    try:
        obj_calculadora = calculadora(int(num1), int(num2))

        otra_operacion = True
        while otra_operacion:
            # pedir operación
            operacion = input("Seleccione la operación (1  +, 2 -, 3 *, 4 /): ")

            if operacion == "1":
                result = obj_calculadora.sumar()
            elif operacion == "2":
                result = obj_calculadora.restar()
            elif operacion == "3":
                result = obj_calculadora.multiplicar()
            elif operacion == "4":
                result = obj_calculadora.dividir()
            else:
                result = None
                print("Operación incorrecta")

            # imprimir resultado si es válido
            if result != None:
                print(f"El resultado de la operacion es {result}")

            # preguntar si desea realizar otra operación
            otra_operacion = (
                input("Desea realizar otra operación con esos números (s/n): ") == "s"
            )
        # fin del while para las operaciones

    # capturar error de división por 0
    except ZeroDivisionError:
        print("No se puede dividir por 0")

    # capturar error de conversión a entero
    except ValueError:
        print("Debe teclear dos números")

    # preguntar si desea continuar
    continuar = input("Desea continuar con otros números (s/n): ") == "s"
# fin del while para continuar con otros números
