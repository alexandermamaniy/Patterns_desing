#!/usr/bin/python3
# coding: utf-8

from ..interfaces.mensajesAbstractFactory import MensajesAbstractFactory
from .preguntasEs import PreguntasEs
from .saludosEs import SaludosEs

class MensajesEsFactory(MensajesAbstractFactory):

    def getPreguntas(self):
        return PreguntasEs()


    def getSaludos(self):
        return SaludosEs()