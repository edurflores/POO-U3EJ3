# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:06:48 2021

@author: Eduardo
"""
import datetime as dt# Para registrar fecha
import csv
import numpy as np # Manejo de arrays
from claseTallerCapacitacion import TallerCapacitacion
from claseInscripcion import Inscripcion

class ArregloTalleres:
    def __init__(self):
        self.__arreTalleres = np.empty(0,dtype=TallerCapacitacion) # Crea arreglo de talleres
    def Carga(self):
        archivo = open('Talleres.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        indice = 0 # Indice elemento arreglo
        for fila in reader:
            if ban == False:    
                cant = int(fila[0])
                self.__arreTalleres.resize(cant) # Establece dimension arreglo
                ban = True
            else:
                idta = int(fila[0])
                nomb = fila[1]
                vac = int(fila[2])
                monto = int(fila[3])
                unTaller = TallerCapacitacion(idta, nomb, vac, monto)
                self.__arreTalleres[indice] = unTaller
                indice += 1
        archivo.close()
        print('Se ha cargado la informacion de los talleres en el arreglo')
    def MuestraTalleres(self):
        print('Informacion de talleres')
        print('ID | \tNombre \t\t| Cantidad vacantes \t| Monto inscripcion')
        print('------------------------------------------------------')
        for i in range(len(self.__arreTalleres)):
            print('{} | {}\t| {}\t|\t{}'.format(int(self.__arreTalleres[i].GetId()),str(self.__arreTalleres[i].GetNombreTall()),int(self.__arreTalleres[i].GetVacantes()),self.__arreTalleres[i].GetMonto()))
            print('------------------------------------------------------')
    def Inscripcion(self,persona):
        self.MuestraTalleres()
        idtal = int(input('Seleccione taller ingresando su ID:'))
        ban = False # Bandera para indicar si el taller existe
        for i in range(len(self.__arreTalleres)):
            if self.__arreTalleres[i].GetId() == idtal:
                ban = True
                if self.__arreTalleres[i].GetVacantes() > 0: # Si hay vacantes
                    fecha = dt.date.today()
                    ficha = Inscripcion(fecha, persona, self.__arreTalleres[i]) # Crea la ficha de inscripcion
                    self.__arreTalleres[i].AgregaInscripto(ficha)
                    print('Inscripcion realizada.')
                    return ficha
                else:
                    print('Error. No hay vacantes en el taller seleccionado. La inscripcion no se registro.')
        if ban == False:
            print('Error. No se encontro el taller. La inscripcion no se registro.')
    def MuestraInscriptos(self): # Consigna 4
        idbuscar = int(input('Ingrese ID de taller:'))
        ban = False # Bandera para indicar si el taller existe
        print('Listado de inscriptos')
        print('------------------------')
        print('Nombre | DNI')
        for i in range(len(self.__arreTalleres)):
            if self.__arreTalleres[i].GetId() == idbuscar:
                fichas = self.__arreTalleres[i].GetFichas()
                for j in range(len(fichas)):
                    persona = fichas[j].GetPersona()
                    print('{} | {}'.format(str(persona.GetNombrePer()),str(persona.GetDocumento())))
                    print('-------------------------------------')
                break
        if ban == False:
            print('Error. No se encontro el taller.')