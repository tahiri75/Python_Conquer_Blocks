print("Hannah Neise")
Hannah_Neise_minutos = int(input("Minutos: "))
Hannah_Neise_segundos = int(input("Segundos: "))
Hannah_Neise_centesimas = int(input("Centesimas: "))
Hannah_Neise_total_segundos = (
    Hannah_Neise_minutos * 60 + Hannah_Neise_segundos + Hannah_Neise_centesimas / 100
)
Hannah_Neise_velocidad = 100 / Hannah_Neise_total_segundos

print("Jackie Narracott")
Jackie_Narracott_minutos = int(input("Minutos: "))
Jackie_Narracott_segundos = int(input("Segundos: "))
Jackie_Narracott_centesimas = int(input("Centesimas: "))
Jackie_Narracott_total_segundos = (
    Jackie_Narracott_minutos * 60
    + Jackie_Narracott_segundos
    + Jackie_Narracott_centesimas / 100
)
Jackie_Narracott_velocidad = 100 / Jackie_Narracott_total_segundos

print("Kimberley Bos")
Kimberley_Bos_minutos = int(input("Minutos: "))
Kimberley_Bos_segundos = int(input("Segundos: "))
Kimberley_Bos_centesimas = int(input("Centesimas: "))
Kimberley_Bos_total_segundos = (
    Kimberley_Bos_minutos * 60 + Kimberley_Bos_segundos + Kimberley_Bos_centesimas / 100
)
Kimberley_Bos_velocidad = 100 / Kimberley_Bos_total_segundos
# formatting the output to show the total seconds and speed with 2 decimal places for each athlete
print(
    "Total de segundos de Hannah Neise: ",
    f"{Hannah_Neise_total_segundos:.2f}",
    " Velocidad: ",
    f"{Hannah_Neise_velocidad:.2f}",
)
print(
    "Total de segundos de Jackie Narracott: ",
    f"{Jackie_Narracott_total_segundos:.2f}",
    " Velocidad: ",
    f"{Jackie_Narracott_velocidad:.2f}",
)
print(
    "Total de segundos de Kimberley Bos: ",
    f"{Kimberley_Bos_total_segundos:.2f}",
    " Velocidad: ",
    f"{Kimberley_Bos_velocidad:.2f}",
)
