# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:16:21 2021

@author: zulac
"""

#%%
from numpy import any,array


#%%
def factorial(x):
    if type(x) != int:
        return 'Error valor. El valor ingresado debe ser un numero entero.'
    elif x < 0:
        return 'Error valor. El valor ingresado debe ser mayor a "0".'
    r = 1
    for i in range(x):
        r *= i+1
    return r

#%%
def potencia(c):
    """Calcula y devuelve el conjunto potencia del
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]



#%%
def combina(m,g,cuotas):
    """
    Toma las cuotas (cuotas), numero de apuestas (m) con las combinaciones
 (g) que se quieren hacer y da las cuotas finales y las posiciones de las
 cuotas que la componen.
 """

    matriz = potencia(cuotas)
    resp=[]
    pos = 0
    combinacion = []
    posicion = range(1, m+1)
    matrizp = potencia(posicion)

    for i in range(len(matriz)):
        if len(matriz[i]) == g:
            for j in range(g):
                if j == 0:
                    combinacion.append(matrizp[i])
                    resp.append(matriz[i][j])
                else:
                    resp[pos] *= matriz[i][j]
            pos = pos + 1

    return resp,combinacion

#%%

def posibilidad(Pos_perdidas,ganancias,posiciones):
    """
    Calculo de ganancias según resultados ipoteticos.

    Parameters
    ----------
    posiciones: TYPE list
        Lista de las combinaciones según su posisición.
    ganancias : TYPE list
        Lista de todas las ganancias.
    Pos_perdidas : TYPE list
        Posiciones de las apuestas perdidas.

    Returns
    -------
    x2 : TYPE
        Ganancias según las apuestas perdidas.
    y2 : TYPE
        Combinaciones según las puestas perdidas.

    """
    n = 0

    x2 = posiciones; y2 = ganancias
    while n < len(Pos_perdidas):
        x = []; y = []
        for i in range(len(x2)):
            if any(array(x2[i]) == Pos_perdidas[n]) == False:
                    x.append(x2[i])
                    y.append(y2[i])

        x2 = x; y2 = y
        n += 1

    return x2, y2

#%%
print('Calculadora de apuestas tipo "Sistema"'.center(30,'-'))

c = 0
#INGRESO DE CANTIDAD DE APUESTAS A EVALUAR
while True:
    try:
        c = int(input('Numero de apuestas: '))
    except ValueError:
        print('[!]'*43,'Valor no valido. Debe digitar un numero.','[!]'*43,sep\
='\n')

    if c > 1 and c < 13:
        break
    else:
        print('[!]'*43,'El numero de apuestas debe ser mayor o igual a 1 y \
menor a 13.','[!]'*43,sep='\n')

#INGRESO DE LAS CUOTAS DE LAS APUESTAS
cuotas = []
while True:
    for i in range(c):
        while True:
            try:
                cuotas.append(float(input(f'Cuota de la {i+1}° apuesta: ')))
                break
            except ValueError:
                print('[!]'*43,'Valor no valido. Agregar el valor de la cuota \
con el signo decimal punto (.).','[!]'*43,sep='\n')
    for i in range(c):
        if i == 0:
            print('-'*21,'|'+'# apuesta'.center(8)+' |'+'Cuota'.center(9)+'|'\
,'-'*22,sep='\n')
        print('|'+f'{i+1}°'.center(9),'|'+f'{cuotas[i]}'.center(9)+'|')
        if i == c-1:
            print('-'*21)

#VERIFICACIÓN DE LAS CUOTAS INGRESADAS
    while True:
        r = str(input('¿Estos son los valores de las apuestas? Si(S) No(N) '))
        if r == 'S' or r == 's' or r == 'N' or r == 'n':
            break
        else:
            print('\nRespuesta no valida. Indicar su respuesta con las letras\
 (S) o (N) únicamente.')
    if r == 'S' or r == 's':
        break

#CALCULO DE TODAS LAS POSIBLES COMBINACIONES ENTRE LAS APUESTAS
combinaciones = []
for i in range(c):
    combinaciones.append(int(factorial(c)/(factorial(i+1)*factorial(c-i-1))))

for i in range(c):
    if i == 0:
        print('-'*21,'|'+'Combinadas'.center(8)+'|'+'Cantidad'.center(8)+'|',\
'-'*21,sep='\n')
    print('|'+f'{i}'.center(9),'|'+f'{combinaciones[i]}'.center(8)+'|')
    if i == c-1:
        print('-'*21)

#CREACIÓN DE LA MATRIZ CON LAS CUOTAS DE TODAS LAS POSIBLES COMBINACIONES
matriz = []
for i in range(c):
    matriz.append(combina(c,i+1,cuotas))

combinadas = []
posiciones = []

for i in range(c):
    combinadas.append(matriz[i][0])
    posiciones.append(matriz[i][1])

#INDICADORES DEL PROCESO AL QUE SE VA A REALIZAR CON LOS DATOS ANTERIORES.
#SOLO TENIENDOSE DOS POSIBILIDADES:
#   1) MISMO VALOR PARA TODAS LAS APUESTAS
#   2) DINERO TOTAL A APOSTAR.
while True:
    try:
        r = int(input('¿Que desea realizar?\n\n1) Colocar el mismo valor\
 a todas las combinaciones de apuestas.\n2) Colocar un valor total a apostar.\
\n\nIndicar respuesta: '))
        if r == 1 or r == 2:
            break
        else:
            print('[!]'*43,'Respuesta no valida. Indicar si desea realizar el\
 primer procedimiento (1) o el segundo procedimiento (2).','[!]'*43,sep='\n')
    except ValueError:
        print('[!]'*43,'Valor no valido. La respuesta indicada no es un numero\
.','[!]'*43,sep='\n')

#PROCEDIMIENTO 1: UN VALOR EQUITATIVO PARA TODAS LAS APUESTAS
res = 'N'
if r == 1:
    while True:
        try:
            r=float(input('¿Qué valor desea agregar a todas las combinaciones\
 $'))
            if r < 500:
                print('[!]'*43,'El valor minimo de apuesta, según la plataform\
a, es de $500.\nDebe aumentar el valor de la apuesta para poder realizarla.',\
'[!]'*43,sep='\n')
            else:
                total=0
                for i in combinaciones:
                    total += i
                total *= r
                while True:
                    try:
                        res=str(input(f'${total} Este es el total de dinero \
que va a invertir ¿Está de acuerdo? Si(S) No(N)\nIndicar respuesta: '))
                        if res == 's' or res == 'S':
                            apuesta = []
                            for i in range(c):
                                apuesta.append(r)
                            break
                        elif res == 'n' or res == 'N':
                            print('\nDisminuir el valor de cada una de las\
 apuestas o disminuir el numero de apuestas que se quieren realizar.')
                            break
                        else:
                            print('[!]'*43,'La respuesta indicada no es valida\
. Digitar (S) para Si o (N) para No.','[!]'*43,sep='\n')
                    except ValueError:
                        print('[!]'*43,'Valor no valido. Digitar (S) para Si o\
 (N) para No.','[!]'*43,sep='\n')
            if res == 's' or res == 'S':
                break
        except ValueError:
            print('[!]'*43,'Debe especificar el valor numerico que va a \
apostar.','[!]'*43,sep='\n')

#PROCEDIMIENTO 2: VALOR TOTAL A APOSTAR
#EN ESTE CASO TAMBIÉN SE TENDRÁN EN CUENTA DOS OPCIONES:
#   1) DAR UN VALOR EQUITATIVO A CADA APUESTA
#   2) REALIZAR UN PROCESO DE PONDERACIÓN PARA CADA UNA DE LAS APUESTAS
else:
    total=0
    totalm=0
#CALCULO DE VALOR TOTAL MÍNIMO AL APOSTAR
    for i in combinaciones:
        totalm += i
    del i
    totalm *= 500
    r = 'N'
#INTRODUCCIÓN DEL VALOR TOTAL A APOSTAR
    while r == 'N' or r == 'n':
        try:
            total=float(input('¿Cual es el valor total a apostar? $'))
            if total < totalm:
                print('[!]'*43,f'El valor total es muy bajo. El valor mínimo\
 que se puede apostar a cada cuota es de $500, entonces el valor mínimo total \
es de ${totalm}. Agregar un valor igual o mayor a este o disminuir la cantidad\
 de apuestas a realizar.','[!]'*43,sep='\n')
            else:
                while True:
                    try:
                        r=str(input('El valor digitado es $'+\
    '{:,.2f}'.format(total)+' ¿Es correcto este valor? Si(S) No(N)\n\nIndicar \
Respuesta: '))
                        if r == 'S' or r == 's' or r == 'N' or r == 'n':
                            break
                        else:
                            print('Valor no valido. Debe responder (S) para \
"Si" o (N) para "No".')
                    except ValueError:
                        print('\nValor no valido. Debe responder (S) para "Si"\
 o (N) para "No".')
        except ValueError:
            print('[!]'*43,'Valor no valido. Debe digitar el valor a apostar \
con el signo decimal punto (.).','[!]'*43,sep='\n')

#ELECCIÓN DE DISTRIBUCIÓN DEL DINERO SEGÚN LA OPCIÓN 1) Y 2)
    while True:
        try:
            r=int(input('¿Como desea distribuir el dinero?\n\n1) De forma \
equitativa\n2) De forma ponderada, teniendo en cuenta la cantidad de \
combinaciones y sus cuotas.\n\nIndicar respuesta: '))
            if r == 1:
                break
            elif r == 2:
                break
            else:
                print('[!]'*43,'El valor digitado no es correcto.','[!]'*43,\
sep='\n')
        except ValueError:
            print('[!]'*43,'Valor no valido. Digitar (1) para la primera \
opción o (2) para la segunda opción.','[!]'*43,sep='\n')

#OPCIÓN 1: DISTRIBUCIÓN EQUITATIVA DEL DINERO
    apuesta = 0
    if r == 1:
        apuesta = []; a = 0
        for i in combinaciones:
            a += i

        for i in range(c):
            apuesta.append(round(total/a,2))

#OPCION 2: DISTRIBUCIÓN PONDERADA PARA CADA UNA DE LAS APUESTAS
    if r == 2:

        promedio = []
        for i in range(len(combinadas)):
            a = 0
            for j in combinadas[i]:
                a += j
            promedio.append(a)

        for i in range(c):
            promedio[i] = promedio[i]/combinaciones[i]

        y = []; x = combinaciones[::-1]
        for i in range(len(combinaciones)):
            a = 0
            for j in range(i+1):
                a += x[j]
            y.append(a)
        y = y[::-1]
        del x,i,j,a

        apuesta = []
        for i in range(c):
            apuesta.append(promedio[i]*y[i])

        y = []; x = apuesta[::-1]
        for i in range(len(apuesta)):
            a = 0
            for j in range(i+1):
                a += x[j]
            y.append(a)
        apuesta = y[::-1]
        del x,i,j,a

        a = 0
        for i in apuesta:
            a += i

        for i in range(len(apuesta)):
            apuesta[i] = apuesta[i]/a
            apuesta[i] = total*apuesta[i]
        del a,i,y
#VERIFICACIÓN DE CADA UNA DE LAS APUESTAS QUE SEAN MAYORES A $500
        totalm = []
        for i in combinaciones:
            totalm.append(i*500)

#PROCESO ITERATIVO PARA REEVALUAR LOS VALORES, SI ALGUNO ES MENOR A $500
        error = []
        for i in range(len(apuesta)):
            error.append(apuesta[i] - totalm[i])
        ciclo = 0; dif = 0; error.sort()
        if error[0] < -3 == True:
            ciclo += 1
        while error[0] < -3:
            dif = 0
            for i in range(c):
                if apuesta[i] < totalm[i]:
                    dif = totalm[i]-apuesta[i]
                    apuesta[i] += dif
                    dif /= c-1
                    for j in range(c):
                        if j != i:
                            apuesta[j] -= dif
            for i in range(len(error)):
                error[i] = apuesta[i]-totalm[i]
            error.sort()
            ciclo += 1

        for i in range(c):
            apuesta[i] = round(apuesta[i]/combinaciones[i],2)

        print(f'\nSe realizaron {ciclo} ciclos para calcular los valores.\n')
        del error,dif,ciclo

#IMPRESIÓN DE LOS VALORES DE CADA APUESTA
print('-'*80)
print('Los valores que debe agregar a las apuestas son:'.center(80))
print('-'*80,'\n')
for i in range(c):
    print('(',f'{i+1}'+'°',')',apuesta[i],'\n')

#CALCULO DE LAS GANACIAS
t = []
for i in range(c):
    for j in range(len(combinadas[i])):
        t.append(apuesta[i]*combinadas[i][j])

tt = round(sum(t),2)

#IMPRESIÓN DE LA GANANCIA MÁXIMA
print('\n','-$-'*36,sep='')
print(('El valor máximo de ganancia es de $'+'{:,.2f}'.format(tt-total))\
.center(106))
print('-$-'*36)

#EVALUACIÓN DE TODAS LAS POSIBILIDADES DE GANANCIA O PERDIDA
pl = []; gl = []; pos = 0

for i in range(len(posiciones)):
    for j in range(len(posiciones[i])):
        pl.append(posiciones[i][j])
        gl.append(round(t[pos],2))
        pos += 1
del pos

matrizp = []
for i in range(len(posiciones)):
    for j in posiciones[i]:
        matrizp.append(posibilidad(j,gl,pl))

matrizs = []
for i in range(len(matrizp)):
    s = 0; x = []
    for j in matrizp[i][1]:
        s += j
    x.append(pl[i]);x.append(round(s,2))
    matrizs.append(x)
del x,i,j,s

#CREACIÓN DE LAS TABLAS DE PERDIDAS Y GANANCIAS SEGÚN CADA EVENTO POSIBLE
matrizp = []; matrizg = [[[],tt]]
for i in range(len(matrizs)):
    x = []
    if matrizs[i][1] < total:
        x.append(matrizs[i][0])
        x.append(round(matrizs[i][1]-total,2))
        matrizp.append(x)
    else:
        x.append(matrizs[i][0])
        x.append(round(matrizs[i][1]-total,2))
        matrizg.append(x)
del x,i

#IMPRESIÓN DE CADA UNA DE LAS TABLAS DE GANANCIA Y PERDIDA
for i in range(len(matrizp)):
    if i == 0:
        print('-'*106)
        print('|','Apuestas perdidas'.center(50),'|','Dinero perdido'\
.center(50),'|')
        print('-'*106)
        print('|',str(matrizp[i][0]).center(50),'|',('$ '+'{:,.2f}'.format(\
matrizp[i][1])).center(50),'|')
    elif i == len(matrizp)-1:
        print('|',str(matrizp[i][0]).center(50),'|',('$ '+'{:,.2f}'.format(\
matrizp[i][1])).center(50),'|')
        print('-'*106)
    else:
        print('|',str(matrizp[i][0]).center(50),'|',('$ '+'{:,.2f}'.format(\
matrizp[i][1])).center(50),'|')

for i in range(len(matrizg)):
    if i == 0:
        print('-'*106)
        print('|','Apuestas perdidas'.center(50),'|','Dinero ganado'\
.center(50),'|')
        print('-'*106)
        print('|',str(matrizg[i][0]).center(50),'|',('$ '+'{:,.2f}'.format(\
matrizg[i][1])).center(50),'|')
    elif i == len(matrizg)-1:
        print('|',str(matrizg[i][0]).center(50),'|',('$ '+'{:,.2f}'.format(\
matrizg[i][1])).center(50),'|')
        print('-'*106)
    else:
        print('|',str(matrizg[i][0]).center(50),'|',('$ '+'{:,.2f}'.format(\
matrizg[i][1])).center(50),'|')

#FINAL DEL PROGRAMA

#%%

n = 0
posiciones = pl
ganancias = gl
Pos_perdidas = [1,2]

x2 = posiciones; y2 = ganancias
while n < len(Pos_perdidas):
    x = []; y = []
    for i in range(len(x2)):
        if any(array(x2[i]) == Pos_perdidas[n]) == False:
                x.append(x2[i])
                y.append(y2[i])

    x2 = x; y2 = y
    n += 1
