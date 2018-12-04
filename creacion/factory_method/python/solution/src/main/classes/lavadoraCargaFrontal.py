#!/usr/bin/python3
# coding: utf-8

from src.main.interfaces.lavadora import Lavadora

class LavadoraCargaFrontal(Lavadora):

    def __init__(self):
        super(LavadoraCargaFrontal, self).__init__()
        self._tipoCarga = "frontal"

