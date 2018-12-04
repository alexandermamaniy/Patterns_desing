#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractmethod

class BuilderMayor(metaclass=ABCMeta):


    @abstractmethod
    def setLugarTrabajo(self, lugarTrabajo):
        pass

    @abstractmethod
    def build(self):
        pass