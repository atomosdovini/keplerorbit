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

def f_(x0, args):
    return x0 - args[1] - args[0] * np.sin(x0)


def f_prime(x0, args):
    return 1 - args[0] * np.cos(x0)

 
def newton_method(f_, f_prime, x0, tol=1e-12, args=[]):
    nmax = 1000
    step = 1

    delta_x = f_(x0, args) / f_prime(x0, args)

    while abs(delta_x) > tol or step < nmax:
        x0 -= abs(delta_x)

        delta_x = f_(x0, args) / f_prime(x0, args)

        step += 1

        return delta_x, step