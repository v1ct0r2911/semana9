#5.	Realice un programa en Python que calcule e imprima la suma, el promedio,
# el mayor y el menor de 5 valores registrados en una lista.
numeros=[]
suma=0
for i in range(5):
    mi_numero=int(input("ingrese un numero: "))
    numeros.append(mi_numero)
for numero in numeros:
    suma+=numero
promedio=suma/len(numeros)
print(suma)
print(promedio)
print(max(numeros))
print(min(numeros))