#!/usr/bin/python3
# coding: utf-8

from ..interfaces.mensajesAbstractFactory import MensajesAbstractFactory
from .preguntasEn import PreguntasEn
from .saludosEn import SaludosEn

class MensajesEnFactory(MensajesAbstractFactory):

    def getPreguntas(self):
        return PreguntasEn()


    def getSaludos(self):
        return SaludosEn()