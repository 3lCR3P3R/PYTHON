import os
from collections import deque
carrito_de_compras = deque()
os.system ("cls")
respuesta = input("¿Deseas comprar algun producto de nuestro mercado?, ¿Si o No?\n")
while respuesta == "Si" or respuesta == "si":
    compra = input("¿Que producto deseas agregar?\n")
    opcion = input("¿desea agregar el producto al carrito?\n¿Si o No?\n")
    while opcion != "Si" or opcion != "si" or opcion != "No" or opcion != "no":
        if opcion == "Si" or opcion == "si":
            carrito_de_compras.append(compra)
            mostrar_Compra = input("¿Deseas ver los articulos del carrito?\n¿Si o No?\n")
            while mostrar_Compra != "Si" or mostrar_Compra != "si" or mostrar_Compra != "No" or mostrar_Compra != "no":
                if mostrar_Compra == "Si" or mostrar_Compra == "si":
                    print(carrito_de_compras)
                    break 
                elif mostrar_Compra == "No" or mostrar_Compra == "no":
                    print("Esta bien querido cliente")
                    break
                else:
                    os.system ("cls")
                    print("Esa opcion no la tengo asignada en mi algoritmo")
                    mostrar_Compra = input("¿Deseas ver los articulos del carrito?\n¿Si o No?\n")
        elif opcion == "No" or opcion == "no":
            print("Esta bien querido cliente")
            break
        else:
                os.system ("cls")
                print("Esa opcion no la tengo asignada en mi algoritmo")
                opcion = input("¿desea agregar el producto al carrito?\n¿Si o No?\n")
    if len(carrito_de_compras) == 0:
        salida = input("¿Deseas salir de la tienda?\n¿Si o No?\n")
        while salida != "Si" or salida != "si" or salida != "No" or salida != "no":
            if salida == "Si" or salida == "si":
                print("hasta la proxima querido cliente")
                break
            elif salida == "No" or salida == "no":
                print("Esta bien querido cliente")
                break
            else:
                os.system ("cls")
                print("Esa opcion no la tengo asignada en mi algoritmo")
                salida = input("¿Deseas salir de la tienda?\n¿Si o No?\n")
    elif len(carrito_de_compras) >= 1:
        comprar_Productos = input("¿Deseas pagar ya tus productos?\n¿Si o No?\n")
        while comprar_Productos != "Si" or comprar_Productos != "si" or comprar_Productos != "No" or comprar_Productos != "no":
            if comprar_Productos == "Si" or comprar_Productos == "si":
                print("Estos son los productos que compraste")
                print(carrito_de_compras)
                print("Gracias por la compra")
                break 
            elif comprar_Productos == "No" or comprar_Productos == "no":
                mostrar_Compra=1
                print("Esta bien querido cliente")
                break
            else:
                os.system ("cls")
                print("Esa opcion no la tengo asignada en mi algoritmo")
                comprar_Productos = input("¿Deseas pagar ya tus productos?\n¿Si o No?\n")
    if len(carrito_de_compras) > 2:
        eliminar_Producto = input("¿Deseas eliminar el primer producto del carrito?\n¿Si o No?\n")
        while salida != "Si" or salida != "si" or salida != "No" or salida != "no":
            if eliminar_Producto == "Si" or eliminar_Producto == "si":
                carrito_de_compras.popleft()
                os.system ("cls")
                print("Estos son los productos que tienes en el carrito")
                print(carrito_de_compras) 
                break
            elif eliminar_Producto == "No" or eliminar_Producto == "no":
                os.system ("cls")
                print("Esta bien querido cliente")
                break
            else:
                os.system ("cls")
                print("Esa opcion no la tengo asignada en mi algoritmo")
else:
    print("hasta la proxima querido cliente")