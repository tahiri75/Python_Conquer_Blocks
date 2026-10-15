# --- crear la lista original ---
originalList = []
listLen = int(input("Teclee la longitud de la lista: "))
for i in range(0, listLen):
    originalList.append(input("Elemento {} de la lista: ".format(i)))

# --- mostrar la lista original ---
print("Lista original:", originalList)

# --- buscar duplicados
duplicateList = []
i = 0
j = i + 1

while i < len(originalList):
    if originalList[i] in duplicateList:
        # --- si el elemento ya está en la lista de duplicados, lo eliminamos de la lista original ---
        originalList.pop(i)
        # print("len: ", len(originalList))
        continue
    else:
        j = i + 1
        while j < len(originalList):
            if (originalList[i] == originalList[j]) and not (
                originalList[i] in duplicateList
            ):
                # --- si el elemento es duplicado y no está en la lista de duplicados, lo añadimos a la lista de duplicados y lo eliminamos de la lista original ---
                duplicateList.append(originalList[j])
                # --- eliminamos el elemento duplicado de la lista original ---
                originalList.pop(j)
                # print("len2: ", len(originalList))
            else:
                j += 1
        i += 1

# --- mostrar la lista de duplicados y la lista sin duplicados ---
print("Lista de duplicados:", duplicateList)
print("Lista sin duplicados:", originalList)
