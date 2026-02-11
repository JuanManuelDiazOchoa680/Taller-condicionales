# Programa para verificar si un número es positivo o negativo o cero

#librerias
import math

#-------
#Input
#-------

print("                                                               ")
print("      Verificar si el numero es positivo, negativo o cero      ")
print("                                                               ")

x=int(input("Digite el valor de x: "))

#processing

if(x>0):
    Rta= "Positivo"

else:
    Rta= "Negativo o cero"

#------
#output
#------

print("                      ")
print("      RESULTADOS      ")
print("                      ")
print("El valor de x es: " +str(Rta))
print("                            ")
