#!/usr/bin/python3
# coding: utf-8

from src.main.classes.builder import Builder

if __name__ == '__main__':

    madre = Builder("Maria").setMunicipio("Selva").setMayor(37).setLugarTrabajo("Google").build()
    print(madre)

    hijo = Builder("Pedro").setMenor(4).setColegio("Colegio de Selva").build()
    print(hijo)

    # esta codigo NO debe compilar

    mal1 = Builder("Luisa").setMayor(20).setColegio("Colegio de Villa Arriba").build();
    #mal2 = Builder("Luisa").setMayor(10).setColegio("Colegio de Villa Arriba").build();