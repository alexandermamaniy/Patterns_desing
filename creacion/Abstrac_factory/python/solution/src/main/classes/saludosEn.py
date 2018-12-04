#!/usr/bin/python3
# coding: utf-8

from ..interfaces.saludos import Saludos

class SaludosEn(Saludos):

    def buenosDias(self):
        return 'good morning'


    def buenasTardes(self):
        return 'good afternoon'

