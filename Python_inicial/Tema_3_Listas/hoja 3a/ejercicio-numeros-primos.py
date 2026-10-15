# --- numeros primos entre 2 y 100 ---
Lista_numeros = []

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0 and i != j:
            break
    else:
        Lista_numeros.append(i)

print("Los números primos entre 2 y 100 son:", Lista_numeros)
