# Progrma para verificar si los 2 ultimos digitos de un numero son iguales

#librerias
import math

#-----
#input
#-----

print("                                                          ")
print("      verificar si los 2 ultimos digitos son iguales      ")
print("                                                          ")

n=int(input("digute el valor de n: "))

#----------
#Processing
#----------

Ud=n%10
Pd=(n//10)%10

if(Ud==Pd):
    Rta="son iguales"

else:
    Rta="No so iguales"

#------
#output
#------

print("                                                ")
print("      RESULTADOS      ")
print("                                                ")
print("el numero es: " +str(n))
print("los dos ultimos digitos: " +str(Rta))
print("                                      ")
