# Programa en Python para calcular el pago de una llamada a travez de cuanto tiempo se demora.

#Librerias
import math

#-----
#Input
#-----

print("                            ")
print("      Costo de llamada      ")
print("                            ")

T=int(input("Digite el tiempo de llamada: "))

#----------
#Processing
#----------

if(T<=3):
    Rta=500 + str("pesos")

else:
    Ta=T-3
    Rta=100*Ta+500

#------
#output
#------

print("                             ")
print("      Resultados     ")
print("                          ")
print("Duracion de la llamada: " +str(T) +str(" min"))
print("                                        ")
print("El costo de la llamada es: " +str(Rta))
print("                                           ")
