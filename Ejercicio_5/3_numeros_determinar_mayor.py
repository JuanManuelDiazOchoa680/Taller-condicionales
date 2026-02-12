# Programa para verificar si entre 3 numeros saber cual es el mayor

#librerias
import math

#-----
#input
#-----

print("                                ")
print("      Verificar cual de los 3 numeros es el mayor      ")
print("                                         ")

A=int(input("digute el valor de A: "))
B=int(input("digute el valor de B: "))
C=int(input("digute el valor de C: "))

#----------
#processing
#----------

if(A>B):
    if(A>C):
        Rta=A
    else:
        Rta=C
else:
    if(B>C):
        Rta=B
    else:
        Rta=C

#------
#output
#------

print("                                 ")
print("      RESULTADOS      ")
print("                           ")
print("El valor de A es: " +str(A))
print("El valor de B es: " +str(B))
print("El valor de C es: " +str(C))
print("                            ")
print("El numero mas grande es: " +str(Rta))
print("                                        ")
