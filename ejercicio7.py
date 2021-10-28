numeros=[]
suma=0
n=int(input("ingrese numero de n"))
for i in range (n):
    mi_numero=int(input("ingrese nuemro:"))
    numeros.append(mi_numero)
suma=0
cont=0
while cont < n:
    suma+=numeros[cont]
    cont+=1
promedio=suma/len(numeros)
print("la suma es: ",suma)
print("el promedio es:", promedio)
print("el mayor es:", max (numeros))
print("el menor es",min(numeros))
