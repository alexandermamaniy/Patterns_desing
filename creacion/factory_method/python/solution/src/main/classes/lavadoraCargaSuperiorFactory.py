#!/usr/bin/python3
# coding: utf-8

from ..interfaces.lavadoraFactory import LavadoraFactory
from .lavadoraCargaSuperior import LavadoraCargaSuperior

class LavadoraCargaSuperiorFactory(LavadoraFactory):


    def creaLavadora(self):
        return LavadoraCargaSuperior()