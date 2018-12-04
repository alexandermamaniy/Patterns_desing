#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractmethod

class MensajesAbstractFactory(metaclass=ABCMeta):

    @abstractmethod
    def getPreguntas(self):
        pass

    @abstractmethod
    def getSaludos(self):
        pass