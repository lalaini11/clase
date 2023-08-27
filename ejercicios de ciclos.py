#Realice un algoritmo que permita calcular la multiplicación de dos números enteros solo usando sumas
k=0
i=int(input("ingrese número: "))
j=int(input("ingrese número: "))
while True:
    k+=i
    j-=1
    if j==0:
        print("el producto es", k)
        break
#Realice un algoritmo que permita calcular a partir de un número de notas, el promedio de una materia, sabiendo que cada nota tiene el mismo porcentaje y están evaluadas de 0 a 5.
s=0
i=1
n=int(input("ingrese la cantidad de notas a promediar: "))
while(i<=n):
    print("ingrese la nota: ",i)
    g = float(input())
    s+=g
    i+=1
p=s/n
print("el promedio de notas es ", p)
#Desarrollar un algoritmo que escriba en pantalla, uno después del otro, los resultados de lafunción n^x desde 0 hasta n, con n entero positivo máximo 9 y x positivo máximo de 9
n=int(input("ingrese un numero: "))
x=int(input("ingrese un numero: "))
k=1
while (n<9):
    k*=n
    x-=1
    if x==0:
        print("la función n^x es ", k)
        break
m=int(input("ingrese un número: "))
k=0
while n<=m:
    if n % 2 ==0:
        print(n)
    n+=1
#Hacer un algoritmo que encuentre la suma de los números impares comprendidos entre 1 y N
n=1
m=int(input("ingrese un número: "))
k=0
while n<=m:
    if n % 2 == 1:
        k=k+n
    n+=1
print("la suma de los números impares es ", k)
#Elaborar un algoritmo que encuentre el factorial de un número comprendido entre 0 y 20. 
#En caso de que se cometa un error o se haya terminado de realizar la tarea solicitada, 
#que el programa de la opción de volver a empezar.
x=int(input("ingrese un número: "))
if x==0:
    print("El factorial es", x)
while x<0:
    print("No se puede calcular.")
    x=int(input("ingrese un número: "))
while x>20:
    print("Ingrese un número menor a 20")
    x=int(input("ingrese un número: "))
else:
    k=1
    factorial=1
    while k<=x:
        factorial= factorial*k
        k=k+1
    print("el factorial del número es ", factorial)
x=int(input("ingrese un número: "))

    