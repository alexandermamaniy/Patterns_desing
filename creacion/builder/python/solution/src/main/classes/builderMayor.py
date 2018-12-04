#!/usr/bin/python3
# coding: utf-8

from ..interfaces import builderMayor


class BuilderMayor(builderMayor.BuilderMayor):

    def __init__(self, persona):
        self._persona = persona

    def setLugarTrabajo(self, lugarTrabajo):
        self._persona.lugarTrabajo = lugarTrabajo
        return self

    def build(self):
        return self._persona