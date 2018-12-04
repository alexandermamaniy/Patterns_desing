#!/usr/bin/python3
# coding: utf-8

from abc import ABCMeta, abstractmethod

class BuilderMenor(metaclass=ABCMeta):


    @abstractmethod
    def setColegio(self, colegio):
        pass

    @abstractmethod
    def build(self):
        pass