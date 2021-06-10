# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:43:09 2021

@author: Eduardo
"""
import csv
import numpy as np
from claseInscripcion import Inscripcion

class ManejadorInscripcion:
    __dimension = 0 # Dimension del arreglo
    __indice = 0
    def __init__(self):
        self.__arreInscripciones = np.empty(self.__dimension,dtype=Inscripcion) # Crea arreglo de fichas de inscripcion
    def GuardaFicha(self,ficha):
        if self.__indice == self.__dimension: # Debera expandirse
            self.__dimension += 1
            self.__arreInscripciones.resize(self.__dimension)
        self.__arreInscripciones[self.__indice] = ficha # Guarda la ficha
        self.__indice += 1
    def ConsultaInscripcion(self,docu): # Consigna 3
        ban = False # Bandera para indicar si se encontro la persona buscada
        for i in range(self.__dimension):
            persona = self.__arreInscripciones[i].GetPersona()
            if persona.GetDocumento() == docu:
                ban = True # La encontro
                taller = self.__arreInscripciones[i].GetTaller()
                print('Taller en el que se inscribio:',taller.GetNombreTall())
                if self.__arreInscripciones[i].GetPago() == False:
                    print('Monto que adeuda:',taller.GetMonto())
                else:
                    print('El inscripto no adeuda monto alguno.')
                break
        if ban == False:
            print('No se encontro el DNI buscado. La persona no esta inscripta.')
    def RegistraPago(self): # Consigna 5
        print('Registrar pago.')
        docu = input('Ingrese DNI:')
        for i in range(len(self.__arreInscripciones)):
            persona = self.__arreInscripciones[i].GetPersona()
            if persona.GetDocumento() == docu:
                if self.__arreInscripciones[i].GetPago() == True: # La persona ya habia pagado.
                    print('El inscripto no adeuda monto (ya pago).')
                    break
                else:
                    self.__arreInscripciones[i].SetPagoTrue() # La persona no pago, entonces se registra el pago
                    break
    def GuardaArchivo(self):
        archivo = open('Inscripciones.csv','w', newline='') # Abrir archivo en modo escritura (si no existe, lo crea)
        writer = csv.writer(archivo, delimiter=',')
        for i in range(len(self.__arreInscripciones)):
            dni = self.__arreInscripciones[i].GetPersona().GetDocumento()
            idtaller = self.__arreInscripciones[i].GetTaller().GetId()
            fecha = self.__arreInscripciones[i].GetFecha()
            pago = self.__arreInscripciones[i].GetPago()
            writer.writerow(dni,idtaller,fecha,pago)
        archivo.close()
        print('Se ha guardado el archivo Inscripciones.csv')