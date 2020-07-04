#!/usr/bin/env python

#Desglosa el valor que se inserte
dinero = sorted([5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000], reverse=True)
cantidadDinero = [0] * len(dinero)
resto = valorImporte = int( input("Ingrese el valor del importe: "))
for i in range( len(dinero)):
    cantidadDinero[i], resto = divmod(resto, dinero[i])
    if cantidadDinero[i] > 0:
        print(f"{cantidadDinero[i]} de {dinero[i]} | ", end="")