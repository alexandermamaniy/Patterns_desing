#!/usr/bin/python3
# coding: utf-8

from src.main.interfaces.lavadora import Lavadora

class LavadoraCargaSuperior(Lavadora):

    def __init__(self):
        super(LavadoraCargaSuperior, self).__init__()
        self._tipoCarga = "superior"