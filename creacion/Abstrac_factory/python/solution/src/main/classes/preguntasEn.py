#!/usr/bin/python3
# coding: utf-8

from ..interfaces.preguntas import Preguntas

class PreguntasEn(Preguntas):


    def preguntaHora(self):
        return 'what time is it?'


    def preguntaTiempo(self):
        return 'how is the weather?'