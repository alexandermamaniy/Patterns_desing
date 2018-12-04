#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractmethod

class Saludos(metaclass=ABCMeta):

    @abstractmethod
    def buenosDias(self):
        pass

    @abstractmethod
    def buenasTardes(self):
        pass
