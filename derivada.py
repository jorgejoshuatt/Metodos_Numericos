import math
def funcion(x):
    resultado=math.e ** x+x
    return resultado

def derivada(x):
    derivada=(funcion(x+h)-funcion(x-h))/(2*h)
    return derivada

def seg_derivada(x):
    sderivada=(funcion(x-h)-2*funcion(x)+funcion(x+h))/(h**2)
    return sderivada

x=float (input("¿En qué valor de x deseas calcular la derivada? "))
h=float(input("Introduce el valor de h: "))
print("Valor de x en la derivada:",derivada(x))
print("Valor de x en la segunda derivada:",seg_derivada(x))