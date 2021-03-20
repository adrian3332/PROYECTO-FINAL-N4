from claseCliente import Cliente
from archivo import Archivo
from menu import Menu
from os import system
import time
def menuCliente():
    system("cls")
    pos = lambda y,x: '\x1b[%d;%dH'%(y,x) 
    men = Menu(['1.- Ingreso', '2.- Listado', '3.- Salir'], '         Menú Grupo')
    opc = men.mostrarMenu()
    while opc != '3':
        system("cls")
        if opc == '1':
           ruc = input("Ruc........:"+pos(1,25))
           nom = input("Nombre.....:"+pos(2,25))
           dir = input("Dirección..:"+pos(3,25))
           tel = input("Telefono...:"+pos(4,25))
           mai = input("Mail.......:"+pos(5,25))
           cliente = Cliente(ruc, nom, dir, tel, mai, est= True)
           arch = Archivo()
           arch.escribir('cliente.txt', cliente.mostrarCliente())
           x = input("Registro Guardado!, Presione una tecla para continuar...")


        elif opc=='2':
            print(pos(1,15) + "Listado de Clientess")
            print("Ruc     Nombre     Dirección     Telefono     Mail")
            arch = Archivo()
            datos = arch.leer('cliente.txt')
            for dato in datos:
                print("{:10s} {:10s}{:10s}{:10s}{:10s}".format(dato[0], dato[1], dato[2],
                dato[3], dato[4]))
            x = input("Presione una tecla para continuar...")
        system("cls")
        opc = men.mostrarMenu()