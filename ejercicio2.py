#2.	Elabore un programa en Python que calcule el promedio de 5 numeros. Emplee listas.

numeros=[10,20,30,40,50]
#promedio de lña lista de numeros
suma=0
for numero in numeros:
    suma+=numero
#la suma de todos los numeros de la lista
promedio=suma /len(numeros)
print(suma)
print(promedio)