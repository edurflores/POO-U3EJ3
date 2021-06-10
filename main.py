# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:09:52 2021

@author: Eduardo
"""
from claseManejadorPersona import ManejadorPersona
from claseArregloTalleres import ArregloTalleres
from claseManejadorInscripcion import ManejadorInscripcion
if __name__ == '__main__':
    mp = ManejadorPersona()
    at = ArregloTalleres()
    mi = ManejadorInscripcion()
    at.Carga() # Consigna 1
    at.MuestraTalleres()
    op = 1
    print('Menu')
    while op != 0:
        print('1- Inscribir persona en un taller (Consigna 2).\n2- Consultar inscripcion de persona (Consigna 3).\n3- Consultar inscriptos de taller (Consigna 4).\n4- Registrar pago (Consigna 5).\n5- Guardar inscripciones (Consigna 6).\n0- Salir del programa.')
        op = int(input('Seleccione opcion:'))
        if op == 1: # Consigna 2
            aux = 1
            while aux != 0:
                persona = mp.RegistraPersona() # Primero carga la persona en la lista correspondiente.
                ficha = at.Inscripcion(persona) # Luego la inscribe en el taller y obtiene su ficha
                mi.GuardaFicha(ficha) # Guarda la ficha.
                print('¿Inscribir otra persona? \n1- Si.\n0- No (terminar).')
                aux = int(input('Opcion:'))
        elif op == 2: # Consigna 3
            docu = input('Ingrese DNI:')
            mi.ConsultaInscripcion(docu)
        elif op == 3: # Consigna 4
            at.MuestraInscriptos()
        elif op == 4: # Consigna 5
            mi.RegistraPago()
        elif op == 5: # Consigna 6
            mi.GuardaArchivo()