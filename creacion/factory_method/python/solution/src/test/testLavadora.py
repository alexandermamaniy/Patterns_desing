#!/usr/bin/python3
# coding: utf-8

from unittest import TestCase
from ..main.classes.lavadoraCargaFrontalFactory import LavadoraCargaFrontalFactory
from ..main.classes.lavadoraCargaSuperiorFactory import LavadoraCargaSuperiorFactory

class TestLavadora(TestCase):

    def test_carga_frontal(self):
        factory = LavadoraCargaFrontalFactory()

        lavadora = factory.crea()

        self.assertEqual("frontal", lavadora.tipoCarga)
        self.assertTrue(lavadora.tieneMandos)
        self.assertTrue(lavadora.tieneTambor)

    def test_carga_superior(self):
        factory = LavadoraCargaSuperiorFactory()
        lavadora = factory.crea()

        self.assertEqual("superior", lavadora.tipoCarga)
        self.assertTrue(lavadora.tieneMandos)
        self.assertTrue(lavadora.tieneTambor)