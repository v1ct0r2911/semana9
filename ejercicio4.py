#4.	Realice un programa en Python que registre 5 numeros y 
# los guarde en una lista y finalizado el registro que calcule 
# el numero mayor y menor contenido en dicha lista.
numeros=[]
for i in range(5):
    num=int(input("ingrese numero"))
    numeros.append(num)
print(max(numeros))
print(min(numeros))