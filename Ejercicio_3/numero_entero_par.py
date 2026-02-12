# Programa en Python para verificar si un numero entero es par o impar

#Librerias
import math

#-----
#input
#-----

print("                                            ")
print("      Verificar si un numero es par o impar      ")
print("                                            ")

n=int(input("Digite el numero: "))

#----------
#Processing
#----------

if(n % 2 == 0):
    Rta="par"

else:
    Rta="impar"

#------
#output
#------

print("                      ")
print("      Resultados      ")
print("                      ")
print("el numero es: " +str(Rta))
print("                      ")
