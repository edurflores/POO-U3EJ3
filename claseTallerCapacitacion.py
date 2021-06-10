# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:14:03 2021

@author: Eduardo
"""

class TallerCapacitacion:
    __idTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0
    __fichasinscriptos = None # Fichas de las personas inscriptas en el taller
    def __init__(self,idta,nomb,vac,monto):
         self.__idTaller = idta
         self.__nombre = nomb
         self.__vacantes = vac
         self.__montoInscripcion = monto
         self.__fichasinscriptos = []
    def GetId(self):
        return self.__idTaller
    def GetNombreTall(self):
        return self.__nombre
    def GetVacantes(self):
        return self.__vacantes
    def GetMonto(self):
        return self.__montoInscripcion
    def GetFichas(self): # Funcion que devuelve los inscriptos al taller
        return self.__fichasinscriptos
    def AgregaInscripto(self,ficha):
        self.__fichasinscriptos.append(ficha)
        self.__vacantes -= 1