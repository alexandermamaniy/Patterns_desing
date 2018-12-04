#!/usr/bin/python3
# coding: utf-8

import unittest
from ..main.classes.mensajeEsFactory import MensajesEsFactory
from ..main.classes.mensajeEnFactory import MensajesEnFactory

class TestMultiIdioma(unittest.TestCase):

    def test_es(self):

        # este es el punto clave del abstrac factory, ya que solo cambiando MensajesEsFactory por MensajesEnFactory,
        # cambiamos por completo la famila de clases, por ejemplo pensemos que cuenta Mensajes Idiomas, estamo manejando
        # Bases de datos, como ser Relacional y no relacional, donde las clases Preguntas y Saludos son metodos para obtener
        # de la base de datos

        # que cabrom XD

        factory = MensajesEsFactory()

        preguntas = factory.getPreguntas()

        self.assertEqual('¿qué hora es?', preguntas.preguntaHora())
        self.assertEqual('¿qué tiempo hace?', preguntas.preguntaTiempo())

        saludos = factory.getSaludos()
        self.assertEqual('buenos días', saludos.buenosDias())
        self.assertEqual('buenas tardes', saludos.buenasTardes())

    def test_en(self):

        factory = MensajesEnFactory()

        preguntas = factory.getPreguntas()

        self.assertEqual('what time is it?', preguntas.preguntaHora())
        self.assertEqual('how is the weather?', preguntas.preguntaTiempo())

        saludos = factory.getSaludos()
        self.assertEqual('good morning', saludos.buenosDias())
        self.assertEqual('good afternoon', saludos.buenasTardes())
