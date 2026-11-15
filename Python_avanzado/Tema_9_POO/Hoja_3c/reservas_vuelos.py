"""'SISTEMA DE RESERVAS DE VUELOS
Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:- Clase base: `Vuelo`
  - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
  - Métodos: agregar pasajero, verificar disponibilidad de asientos
  - Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
  - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales."""


class Vuelo:
    # clase para reservas de vuelo
    def __init__(self, numero_vuelo, origen, destino, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    # métodos de la clase
    def verificar_diponibilidad(self):
        return self.capacidad - len(self.pasajeros)

    def agregar_pasajero(self, pasajero):
        if self.verificar_diponibilidad() > 0:
            self.pasajeros.append(pasajero)
            print(f"Pasajero {pasajero} agregado al vuelo {self.numero_vuelo}")

        else:
            print("No hay disponibilidad")


class VueloEspecial(Vuelo):
    # clase para vuelos especiales, hereda de la clase Vuelo
    def __init__(self, numero_vuelo, origen, destino, capacidad, motivo):
        super().__init__(numero_vuelo, origen, destino, capacidad)
        self.motivo = motivo


vuelo_regular = Vuelo("IB123", "Madrid", "Barcelona", 100)
vuelo_regular.agregar_pasajero("Juan Pérez")

vuelo_especial = VueloEspecial("IB456", "Madrid", "París", 50, "Vacaciones")
vuelo_especial.agregar_pasajero("María García")

print(
    f"Vuelo regular {vuelo_regular.numero_vuelo} tiene {vuelo_regular.verificar_diponibilidad()} asientos disponibles."
)
print(
    f"Vuelo especial {vuelo_especial.numero_vuelo} tiene {vuelo_especial.verificar_diponibilidad()} asientos disponibles y el motivo es {vuelo_especial.motivo}"
)
