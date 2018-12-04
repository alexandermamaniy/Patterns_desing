#!/usr/bin/python3
# coding: utf-8

from ..interfaces import builder
from .persona import Persona
from .builderMayor import BuilderMayor
from .builderMenor import BuilderMenor

class Builder(builder.Builder):

    def __init__(self, nombre):
        self._persona = Persona()
        self._persona.nombre = nombre

    def setMunicipio(self, municipio):
        self._persona.municipio = municipio
        return self

    def setMayor(self, edad):
        if edad <18 :
            raise Exception('no es mayor de 18')

        self._persona.edad = edad
        return BuilderMayor(self._persona)

    def setMenor(self, edad):
        if edad >= 18 :
            raise Exception('no es menor de 18')

        self._persona.edad = edad
        return BuilderMenor(self._persona)