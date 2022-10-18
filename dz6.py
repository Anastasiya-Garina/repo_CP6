#ДО
a = int(input("Введите размерность массива (число > 0): "))
massiv = []
for i in range(a):
    chiclo = float(input("Введите число: ", ))
    massiv.append(chiclo)
#print(massiv)

maxim = max(massiv)
ind = massiv.index(maxim)
#print(maxim, ind)

for i in range(ind+1, a):
    massiv[i] = 0
    i += 1
print(massiv)

#ПОСЛЕ
def f(a): #функция (создание массива)
    massiv = []
    for i in range(a):
        chiclo = float(input("Введите число: ", ))
        massiv.append(chiclo)
    return massiv

a = int(input("Введите размерность массива (число > 0): "))

massiv = f(a)
maxim = max(massiv)
ind = massiv.index(maxim)
#print(maxim, ind)

for i in range(ind+1, a):
    massiv[i] = 0
    i += 1
print(massiv)