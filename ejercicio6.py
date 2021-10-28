#6.	Elabore un programa en Python que registre 5 numeros en un arreglo 
# e imprima dichos valores del arreglo de forma invertida a lo ingresado (emplee while).
numeros=[]
for i in range(5):
    mi_numero=int(input("ingrese numero: "))
    numeros.append(mi_numero)
for item in reversed(numeros):
    print(item)