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
import math as math
posicoes = 30
r = np.zeros(posicoes)

# encontra o paramtro XC da matriz
def xc_finder(x):
    xc = -(x[1]) / (2 * (x[0]))
    xcentro = xc
    print('\n\n Parametro (xc) da elipse:\n %0.3f' % (xcentro))
    return xcentro


# encontra o paramtro a da matriz
def a_elipse_finder(xcentro, x):
    ae = (((xcentro) ** (2)) - ((x[2]) / (x[0]))) ** (1 / 2)
    aelipse = ae
    print('\n\n Parametro (a) da elipse:\n %0.3f' % (aelipse))
    return aelipse


# encontra o paramtro b da matriz
def b_elipse_finder(aelipse, x):
    be = aelipse * ((-(x[0])) ** (1 / 2))
    belipse = be
    print('\n\n Parametro (b) da elipse:\n %0.3f' % (belipse))
    return belipse



# encontra a excentricidade da matriz
def excentricidade_finder(aelipse, belipse):
    excentricidade = (1 - ((1000 * belipse ** 2) / (1000 * aelipse ** 2))) ** (1 / 2)
    print('\nexcentricidade:\n', (excentricidade))
    return excentricidade


# encontra o foco da matriz
def foco_f(aelipse, excentricidade):
    foco = aelipse * excentricidade
    print('\nfoco:\n', foco)
    return foco


# encontra o periodo
def periodo_elipse(aelipse):
    periodo = (2 * math.pi) * ((((aelipse) ** 3) / (float(6.693) * (10 ** (-11)) * float(5.972) * (10 ** 24))) ** (1 / 2))
    print('\npi:\n', (math.pi))

    print('\nperiodo:\n', (periodo))
    return periodo



def distancia_r(aelipse,excentricidade,ano_verdadeira):
     for i in range(posicoes):
         raio = aelipse*((1-(excentricidade**2))/(1+excentricidade*np.cos(ano_verdadeira[i])))
         r[i] = raio
     print('\ndistancia r:\n',r)
     return r
