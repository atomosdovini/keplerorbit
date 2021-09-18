import numpy as np
from matplotlib import pyplot as plt
import math as math
import interpolacao,parametro,gauss,newton,anomalia,posicao

#declaracao de váriaveis
n = 3
xy = np.zeros(n * 2)
a = np.zeros((n, n + 1))
x = np.zeros(n)
excentricidade = np.zeros(1)
xc = np.zeros(1)
posicoes = 30
ano_media = np.zeros(posicoes)
ano_excentrica = np.zeros(posicoes)
ano_verdadeira = np.zeros(posicoes)
r = np.zeros(posicoes)
n_spline = 3
x1_spline = np.zeros(n_spline)
y1_spline = np.zeros(n_spline)
x2_spline = np.zeros(n_spline)
y2_spline = np.zeros(n_spline)
X = x1_spline
Y = y1_spline
X2 = x2_spline
Y2 = y2_spline


#dados do problema
xy[0] = 20621.3
xy[1] = 34642.3
xy[2] = 21168.5
xy[3] = 5214.2009061
xy[4] = 3201.7095080
xy[5] = 5193.6201775

def arranje_matriz(a, b):
    for i in range(3):
        for j in range(3):
            a[i][0] = xy[i] ** 2
    for i in range(3):
        for j in range(3):
            a[i][1] = xy[i]
    for i in range(3):
        for j in range(3):
            a[i][2] = 1
    a[0][3] = xy[3] ** 2
    a[1][3] = xy[4] ** 2
    a[2][3] = xy[5] ** 2
    print('\n matriz aplicada (a):\n', (a))
    while a[0][0] == 0:
        print('\n pivo=0\n', (a))
        helplist = a[0].copy()
        a[0] = a[1]
        a[1] = helplist
        print('\n nova matriz')    
    return a



a = arranje_matriz(a, xy)
a = gauss.gauss_elimination(a)
x = gauss.regression(a, n)
x = gauss.solution(n)
xcentro = parametro.xc_finder(x)
aelipse = parametro.a_elipse_finder(xcentro, x)
belipse = parametro.b_elipse_finder(aelipse, x)
excentricidade = parametro.excentricidade_finder(aelipse, belipse)
foco = parametro.foco_f(aelipse, excentricidade)
periodo = parametro.periodo_elipse(aelipse)
ano_media = anomalia.anomalia_media(periodo,posicoes)
ano_excentrica = anomalia.anomalia_excentrica(newton.f_, newton.f_prime, newton.newton_method, ano_media, excentricidade)
ano_verdadeira = anomalia.anomalia_verdadeira(ano_excentrica, excentricidade)
r = parametro.distancia_r(aelipse,excentricidade,ano_verdadeira)
pos_y = posicao.posicao_y(r,ano_verdadeira)
pos_x = posicao.posicao_x(r,ano_verdadeira,xcentro,foco)



#função para calcular área deve ser analisada mais a fundo
def area_spline(coef,pos_x):
#   print('\na', a)
    for i in range(2):
        x = pos_x[i]
        x1 = pos_x[i+1]       
        a[i] = coef[i]
        area = abs(a[i+1]*x - a[i]*x)
    return area[i]
    
#def area_spline(coef,posi_x):
#    for i in range(2):
#        x = posi_x[i]
#        x1 = posi_x[i+1]  
#        area = coef[i][0] + ((coef[i][1]*(x-x1)**2)/2) + ((coef[i][2]*(x-x1)**3)/3) + ((coef[i][3]*(x-x1)**4)/4) 
#    return area


for i in range(n_spline):
   x1_spline[i] = pos_x[i] 
   y1_spline[i] = pos_y[i] 
   x2_spline[i] = pos_x[i+2] 
   y2_spline[i] = pos_y[i+2]

coef1 = interpolacao.solve_spline( X, Y, derivatives=[0,0], verbose=True )
coef2 = interpolacao.solve_spline( X2, Y2, derivatives=[0,0], verbose=True )
area1 = area_spline(coef1, x1_spline)
print('\narea 1:\n', area1)
area2 = area_spline(coef2, x2_spline)
print('\narea 2:\n', area2)
X = x1_spline
Y = y1_spline
nn = 100*len(X)
xx = np.linspace(X[0],X[-1],nn)
yy = interpolacao.calc_spline( X, xx, coef1 )
nn2 = 100*len(X2)
xx2 = np.linspace(X2[0],X2[-1],nn2)
yy2 = interpolacao.calc_spline( X2, xx2, coef2 )


if area1 == area2:
    print('\nequações de kepler válidas\n')

else:
    print('\nhá algo de errado, as áreas calculadas não batem\n')


y=0 
t = np.linspace(0, 2*math.pi, 100)
plt.plot( xcentro+aelipse*np.cos(t) , y+belipse*np.sin(t) )
plt.scatter(pos_x,pos_y, marker='o', color='b' ) #em azul
plt.grid(color='lightgray',linestyle='--')
plt.plot( foco , 0 , "o" ) #em laranja
plt.plot( X , Y , "o", color='m' )
plt.plot( xx, yy, "-", color='m' )
plt.plot( X2 , Y2 , "o", color='c' )
plt.plot( xx2, yy2, "-", color='c' )
plt.margins(0.1)
plt.show()


