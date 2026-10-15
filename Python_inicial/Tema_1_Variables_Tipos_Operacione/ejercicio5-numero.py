numero = str(input("Número de más de una cifra: "))
for i in range(len(numero)):
    print(numero[i])
# Print from the last digit to the first digit in same line, using for
for i in range(len(numero) - 1, -1, -1):
    print(numero[i], end="")
print()
# Print from the last digit to the first digit in same line, using ::-1
print(numero[::-1])
print()  # Print a newline at the end
