# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:42:52 2021

@author: Eduardo
"""
from clasePersona import Persona

class ManejadorPersona:
    def __init__(self):
        self.__listaPersonas = []
    def AgregaPersona(self,persona):
        self.__listaPersonas.append(persona)
    def RegistraPersona(self):
        print('Ingrese datos de persona a inscribir.')
        nom = input('Nombre:')
        direc = input('Direccion:')
        docu = input('DNI:')
        unaPersona = Persona(nom, direc, docu)
        self.AgregaPersona(unaPersona)
        return unaPersona