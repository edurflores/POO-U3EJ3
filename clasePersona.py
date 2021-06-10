# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:12:49 2021

@author: Eduardo
"""

class Persona:
    __nombre = ''
    __direccion = ''
    __dni = ''
    def __init__(self,nom,direc,docu):
        self.__nombre = nom
        self.__direccion = direc
        self.__dni = docu
    def GetDocumento(self):
        return self.__dni
    def GetNombrePer(self):
        return self.__nombre