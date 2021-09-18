#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Algoritmo para arranjar a matriz
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Departamento de Engenharias da Mobilidade
# Curso de Cálculo Numérico
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import numpy as np
import math

posicoes = 30
ano_media = np.zeros(posicoes)
ano_excentrica = np.zeros(posicoes)

ano_verdadeira = np.zeros(posicoes) 
def anomalia_media(periodo,posicoes):

    t = float(periodo) / posicoes
    d2r = np.pi / 180.0

    for i in range(posicoes):
        ano_media[i] = (((2 * math.pi) / periodo) * t)*d2r
        for i in range(posicoes):
            t += t
    print('\nanomalia media:\n', (ano_media))
    return ano_media


def anomalia_excentrica(f_, f_prime, newton, ano_media, excentricidade):
    e = excentricidade
    for j in range(posicoes):
        Me = ano_media[j]
        E0 = Me
        args = [e, Me]
        # print('\n----------------------\n',)
        E, steps = newton(f_, f_prime, E0, args=args)
        ano_excentrica[j] = E
    print('\nanomalia excentrica\n', ano_excentrica)
    # print('\nanomalia excentrica encontra steps, rad: \n', (steps, E))

    return ano_excentrica


def anomalia_verdadeira(ano_excentrica, excentricidade):
    for i in range(posicoes):
        x = 2 * (np.arctan(((1+excentricidade)/(1-excentricidade)**1/2)*np.tan(ano_excentrica[i]/2)))
       # x = (np.cos(ano_excentrica[i]) - excentricidade) / (1 - (excentricidade * np.cos(ano_excentrica[i])))
        ano_verdadeira[i] = 1 / np.cos(x)

    print('\nanomalia verdadeira\n', ano_verdadeira)
    return ano_verdadeira