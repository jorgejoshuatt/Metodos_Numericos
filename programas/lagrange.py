import sympy
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def formula(i, j):
    #Argumento de las bases polinómicas de lagrange
    xs = sympy.symbols('x')     # Variable simbólica
    return (xs-x[i]) / (x[j]-x[i]) if i != j else 1  #fórmula
def interpolacion_lagrange(x, y, num_puntos=100):
    """ Estima la curva generada por el polinomio de lagrange que 
    interpola los puntos datos
    """
    xs= sympy.symbols('x') # Variable simbólica
    points = len(x) # Número de puntos ingresados

    #Funciones cardinales lj = [l1, l2, ..., lk]
    lj = []
    for k in range(points):
        lk = np.prod([formula(i, k) for i in range(points)])
        lj.append(lk)
   
    pol = sum(y*lj)  # Polinomio de lagrange
    
    # Se generan los datos X y Y para generar las parábolas de cada punto
    x_p = np.linspace(min(x), max(x), num_puntos) 
    y_p = [pol.subs(xs, i) for i in x_p]    
    return x_p, y_p #Puntos (x, y) estimados a partir del polinomio encontrado. 

#Aquí se ingresan los datos   
x1=[]
y1=[]
n=int(input("¿Cuántos puntos desea ingresar? "))
for i in range(0,n):
        x1.append(int(input(f"Introduzca la coordenada {i} en x: "))) #Coordenadas en x
        y1.append(int(input(f"Introduzca la coordenada {i} en y: "))) #Coordenadas en y
x=np.array(x1)
y=np.array(y1) 
x_p, y_p = interpolacion_lagrange(x, y) # Puntos generados por el polinomio de Lagrange

# Gráfica
plt.plot(x_p, y_p, color='red') #Gráfica la parábola
plt.scatter(x, y, color='blue') #Gráfica los puntos
plt.legend(['Lagrange', 'Puntos'], loc='best') #Gráfica los datos de la gráfica