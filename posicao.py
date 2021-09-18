
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
pos_x = np.zeros(posicoes)
pos_y = np.zeros(posicoes)

def posicao_y(r,ano_verdadeira):
    for j in range(posicoes):
        posicaoy = r[j]*np.sin(ano_verdadeira[j])
        pos_y[j] = posicaoy
    print('\nposição y\n',pos_y)
    return pos_y

def posicao_x(r,ano_verdadeira,xcentro,foco):
    for i in range(posicoes):
        posicaox = r[i]*np.cos(ano_verdadeira[i])+xcentro+foco
        pos_x[i] = posicaox
    print('\nposição x\n',pos_x)
    return pos_x
