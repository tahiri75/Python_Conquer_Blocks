nombre = str(input("Teclee su nombre: "))
print("Hola ", nombre, "!")

# pedir datos del salario
salarioXhoras = float(input("Salario ganado  por horas: "))
horasXsemana = int(input("Horas trabajadas en la semana: "))

# calculo de salario anual suponiendo que hay 4 semanas en el mes y 12 meses en el año
salarioSemanal = salarioXhoras * horasXsemana
salarioMensual = salarioSemanal * 4
salarioAnual = salarioMensual * 12
print(nombre, " tiene unas ganancias anuales de: ", salarioAnual, " euros")

# pedir datos de los gastos
gastosXsemana = float(input("Cuales son sus gastos semanales: "))

# calculo del gasto anual
gastoAnual = gastosXsemana * 4 * 12
print(nombre, " tiene unos gastos anuales de: ", gastoAnual, " euros")

# calculo del ahorro anual
ahorroAnual = salarioAnual - gastoAnual
print(nombre, " tiene un ahorro anual de: ", ahorroAnual, " euros")
