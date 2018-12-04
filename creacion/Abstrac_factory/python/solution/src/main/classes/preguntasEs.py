#!/usr/bin/python3
# coding: utf-8

from ..interfaces.preguntas import Preguntas

class PreguntasEs(Preguntas):


    def preguntaHora(self):
        return '¿qué hora es?'


    def preguntaTiempo(self):
        return '¿qué tiempo hace?'