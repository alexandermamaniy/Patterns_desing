#!/usr/bin/python3
# coding: utf-8

from ..interfaces.lavadoraFactory import LavadoraFactory
from .lavadoraCargaFrontal import LavadoraCargaFrontal

class LavadoraCargaFrontalFactory(LavadoraFactory):


    def creaLavadora(self):
        return LavadoraCargaFrontal()