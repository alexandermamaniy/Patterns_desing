#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta

class Lavadora(metaclass=ABCMeta):

    def __init__(self):
        self._tieneTambor = None
        self._tieneMandos = None
        self._tipoCarga = None

    def ponerTambor(self):
        self._tieneTambor = True


    def ponerMandos(self):
        self._tieneMandos = True


    # setters and getters

    @property
    def tieneTambor(self):
        return self._tieneTambor

    @tieneTambor.setter
    def tieneTambor(self, tieneTambor):
        self._tieneTambor = tieneTambor

    @property
    def tieneMandos(self):
        return self._tieneMandos

    @tieneMandos.setter
    def tieneMandos(self, tieneMandos):
        self._tieneMandos = tieneMandos

    @property
    def tipoCarga(self):
        return self._tipoCarga

    @tipoCarga.setter
    def tipoCarga(self, tipoCarga):
        self._tipoCarga = tipoCarga

