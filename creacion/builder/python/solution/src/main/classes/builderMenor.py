#!/usr/bin/python3
# coding: utf-8

from ..interfaces import builderMenor


class BuilderMenor(builderMenor.BuilderMenor):

    def __init__(self, persona):
        self._persona = persona

    def setColegio(self, colegio):
        self._persona.colegio = colegio
        return self

    def build(self):
        return self._persona