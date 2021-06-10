# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:16:43 2021

@author: Eduardo
"""

from datetime import date

class Inscripcion: # Informacion de la ficha de inscripcion
    __fechaInscripcion = date
    __pago = bool
    __persona = None # Objeto de clase persona
    __taller = None # Objeto de clase taller, al que se inscribio
    def __init__(self,fecha,persona,taller):
        self.__fechaInscripcion = fecha
        self.__pago = False
        self.__persona = persona
    def GetPersona(self):
        return self.__persona
    def GetTaller(self):
        return self.__taller
    def GetPago(self):
        return self.__pago
    def GetFecha(self):
        return self.__fechaInscripcion
    def SetPagoTrue(self):
        self.__pago = True
        print('Se registro el pago.')