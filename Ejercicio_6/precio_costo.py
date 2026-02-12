# Programa en Python para cacular el precio_venta de un producto

#Librerias
import math

#------
#input
#------

print("                                               ")
print("      calcular precio venta de un prducto      ")
print("                                               ")

Pc=int(input("Digite el precio costo del produto: "))

#----------
#processing
#----------

if(Pc<3000):
    Pv=(Pc*0.15)+Pc

else:
    if(Pc>6000):
        Pv=(Pc*0.25)+Pc
    
    else:
        Pv=Pc+500

#-----
#output
#-----

print("                                    ")
print("      Resultados      ")
print("                              ")
print("El precio de venta es: " +str(Pv))
print("                                 ")
