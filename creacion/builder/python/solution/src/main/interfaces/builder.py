#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def setMunicipio(self, municipio):
        pass

    @abstractmethod
    def setMayor(self, edad):
        pass

    @abstractmethod
    def setMenor(self, edad):
        pass

