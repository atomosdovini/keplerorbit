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
n = 3
x = np.zeros(n)

def gauss_elimination(a):
    for i in range(n):
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    print('\n matriz pivotada:\n', (a))

    return a



# realiza substituição regressiva na matriz escalonada
def regression(a, n):
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]
    return x


# print, incógnitas iniciais das equações lineares, em função de x0, x1 , x2
def solution(n):
    print('\na solução é: ')
    for i in range(n):
        print('X%d = %0.3f' % (i, x[i]), end='\t')
    return x
