#!/usr/bin/python3
# coding: utf-8

from ..interfaces.saludos import Saludos

class SaludosEs(Saludos):

    def buenosDias(self):
        return 'buenos días'


    def buenasTardes(self):
        return 'buenas tardes'

