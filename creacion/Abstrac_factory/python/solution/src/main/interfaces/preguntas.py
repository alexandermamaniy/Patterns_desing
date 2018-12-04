#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractmethod

class Preguntas(metaclass=ABCMeta):

    @abstractmethod
    def preguntaHora(self):
        pass

    @abstractmethod
    def preguntaTiempo(self):
        pass