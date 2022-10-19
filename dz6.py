#ДО
size = int(input("Введите размерность массива (число > 0): "))
massiv = []
for i in range(size):
    chiclo = float(input("Введите число: ", ))
    massiv.append(chiclo)
#print(massiv)

maxim = max(massiv)
ind = massiv.index(maxim)
#print(maxim, ind)

for i in range(ind+1, size):
    massiv[i] = 0
    i += 1
print(massiv)

#ПОСЛЕ
def f(size): #функция (создание массива)
    massiv = []
    for i in range(size):
        chiclo = float(input("Введите число: ", ))
        massiv.append(chiclo)
    return massiv

size = int(input("Введите размерность массива (число > 0): "))

massiv = f(size)
maxim = max(massiv)
ind = massiv.index(maxim)
#print(maxim, ind)

for i in range(ind+1, size):
    massiv[i] = 0
    i += 1
print(massiv)