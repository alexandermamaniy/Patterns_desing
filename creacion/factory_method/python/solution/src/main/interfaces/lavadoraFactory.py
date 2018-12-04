#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractmethod

class LavadoraFactory(metaclass=ABCMeta):

    def crea(self):

        lavadora = self.creaLavadora()
        lavadora.ponerTambor()
        lavadora.ponerMandos()
        return lavadora

    @abstractmethod
    def creaLavadora(self):
        pass