#3.	Realice un programa en Python que registre 5 numeros y los guarde en una lista y 
# finalizado el registro que calcule el numero mayor contenido en la lista.
numeros=[]
for i in range(5):
    mi_numero=int(input("ingrese numero: "))
    numeros.append(mi_numero)
print(max(numeros))    