from math import *
 
#Definimos la funcion
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def simpson(n, a, b, f):
    #calculamos h
    h = (b - a) / n
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, n):
        #calculamos la x
        #x = a - h + (2 * h * i)
        x = a + i * h
        # si es par se multiplica por 4
        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 4 * fx(x, f)
    #sumamos los el primer elemento y el ultimo
    suma = suma + fx(a, f) + fx(b, f)
    #Multiplicamos por h/3
    rest = suma * (h / 3)
    #Retornamos el resultado
    return (rest)
 
#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)
 
#valores de ejemplo para la funcion sin(x) con intervalos de
n = 100
a = 2.0
b = 6.0
f = 'log(x)'
 
print(f"Valor aproximado de la integral definida {f} con intervalo de {a} a {b}:", simpson(n, a, b, f))