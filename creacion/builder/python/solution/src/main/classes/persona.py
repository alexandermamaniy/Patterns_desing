#!/usr/bin/python3
# coding: utf-8

class Persona:

    def __init__(self):

        self._nombre = None
        self._edad = None
        self._municipio = None
        self._colegio = None
        self._lugarTrabajo = None

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


    @property
    def municipio(self):
        return self._municipio


    @municipio.setter
    def municipio(self, municipio):
        self._municipio = municipio


    @property
    def colegio(self):
        return self._colegio


    @colegio.setter
    def colegio(self, colegio):
        self._colegio = colegio


    @property
    def lugarTrabajo (self):
        return self._lugarTrabajo


    @nombre.setter
    def lugarTrabajo (self, lugarTrabajo ):
        self._lugarTrabajo  = lugarTrabajo

