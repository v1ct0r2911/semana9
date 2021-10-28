#1.	Elabore un programa en Python que genere 2 listas de  5 elementos cada uno 
# 5 cursos y su respectivo promedio) e imprima sus valores de cada una de las listas

cursos=["python","java","c++","c#","avascrip"]
promedios=[15.4,18.5,16.5,18.5,16.5]
contador=0
for curso in cursos:
    print(curso,promedios[contador])
    contador+=1