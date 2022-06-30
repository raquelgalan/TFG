# TFG Raquel Galán Montes
## Cálculo del Aislamiento a Ruido de Impactos UNE-EN ISO 16283-2:2018 ISO 717-2:2013

from openpyxl import load_workbook      # Permite leer ficheros .xlsx
import math                             # Permite usar funciones matemáticas
from pylab import *                     # Permite crear gráficas
from TR import *                        # Se importa el TR del programa

# VARIABLES GLOBALES
APARTADO = 'Datos'                      # Hoja del archivo XLSX
FILE_Impactos = 'Ruido_Impactos.xlsx'   # Variable para el fichero principal

# ARRAY con constantes
## Rango de frecuencias de interes:
arrayFR = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000]

# Arrays vacíos
L_Impacto_F1 = []        # Array para los resultados del nivel de ruido de impacto en recepción de la fuente en la posición 1
L_Impacto_F2 = []        # Array para los resultados del nivel de ruido de impacto en recepción de la fuente en la posición 2
L_Impacto_F3 = []        # Array para los resultados del nivel de ruido de impacto en recepción de la fuente en la posición 3
L_Impacto_F4 = []        # Array para los resultados del nivel de ruido de impacto en recepción de la fuente en la posición 4
TR = []                  # Array para los resultados del tiempo de reverberación en recepción
LpRF1 = []               # Array para los resultados del nivel de ruido de fondo en la posición 1
LpRF2 = []               # Array para los resultados del nivel de ruido de fondo en la posición 2
LpRF3 = []               # Array para los resultados del nivel de ruido de fondo en la posición 3
LpRF4 = []               # Array para los resultados del nivel de ruido de fondo en la posición 4
LpRC_F1 = []             # Array para los resultados del nivel de ruido de impacto corregido en la posición 1
LpRC_F2 = []             # Array para los resultados del nivel de ruido de impacto corregido en la posición 2
LpRC_F3 = []             # Array para los resultados del nivel de ruido de impacto corregido en la posición 3
LpRC_F4 = []             # Array para los resultados del nivel de ruido de impacto corregido en la posición 4


## PROCEDIMIENTOS ESPECÍFICOS DE LA ISO 16283-2
# Cálculo del promedio de los niveles de ruido de impacto con posiciones de micrófono
# en cada banda de frecuencia, Lp, donde A: min_row; B: max_row; C: min_col; D: max_col; n: posiciones de micrófono

def Calcular_L(A, B, C, D, n, myArray):
    wb = load_workbook(FILE_Impactos)        # Se carga en wb el fichero
    apartado = wb[APARTADO]                  # Se carga la hoja del fichero de donde obtenemos los datos

    for value in apartado.iter_rows(min_row =A, max_row =B, min_col = C, max_col =D,
                                 values_only=True):
        i = 0
        L = 0
        for cell in value:
            L = L + 10**(value[i]/10)       # Se calcula de 10*(Lp/10) y se añade al resultado anterior
            i = i + 1
        L = 10*math.log(L/n,(10))           # Se calcula el promedio logarítmico de la suma total
        myArray.append(round(L,1))          # Array ordenado de datos                 

# Corrección del ruido de fondo:
def LCorregido(A, B, myArray):
    i = 0
    h = 10
    l = 6
    correccion = 1.3
    for num in A:
        dif = A[i] - B[i]
        if dif >= h:
            corregido = A[i]
            myArray.append(round(corregido,2))
            i = i + 1
        elif dif <= l:
            corregido_menor = A[i] - correccion
            myArray.append(round(corregido_menor,2))
            i = i + 1
        else:
            corregido_mayor = (10*math.log(10**(A[i]/10)-10**(B[i]/10),10))  
            myArray.append(round(corregido_mayor,1))
            i = i + 1

# Se preparan los resultados para imprimirlos por pantalla
def Valores(myArray, unidades):
    i = 0                                             # Se inicializa el iterador de los arrays
    for num in arrayFR:
        print(arrayFR[i], 'Hz - ', myArray[i], 'dB')  # Se imprime por la terminal el elemento i del array
        i = i + 1                                     # Siguiente elemento

# Se imprimen todos los datos
if __name__ == "__main__":

    print()
    print('L | MÁQUINA DE IMPACTOS | POSICIÓN 1 DE LA FUENTE')
    print('---------------------------------------------------')
    Calcular_L(33, 53, 7, 8, 2, L_Impacto_F1)
    Valores(L_Impacto_F1, 'dB')

    print()
    print('L | MÁQUINA DE IMPACTOS | POSICIÓN 2 DE LA FUENTE')
    print('---------------------------------------------------')
    Calcular_L(33, 53, 9, 10, 2, L_Impacto_F2)
    Valores(L_Impacto_F2, 'dB')

    print()
    print('L | MÁQUINA DE IMPACTOS | POSICIÓN 3 DE LA FUENTE')
    print('---------------------------------------------------')
    Calcular_L(33, 53, 11, 12, 2, L_Impacto_F3)
    Valores(L_Impacto_F3, 'dB')

    print()
    print('L | MÁQUINA DE IMPACTOS | POSICIÓN 4 DE LA FUENTE')
    print('---------------------------------------------------')
    Calcular_L(33, 53, 13, 14, 2, L_Impacto_F4)
    Valores(L_Impacto_F4, 'dB')

    print()
    print('RUIDO DE FONDO EN HABITACIÓN SUPERIOR | POSICIÓN 1 DE LA FUENTE')
    print('-----------------------------------------------------------------')
    Calcular_L(8, 28, 7, 8, 2, LpRF1)
    Valores(LpRF1, 'dB')

    print()
    print('RUIDO DE FONDO EN HABITACIÓN SUPERIOR | POSICIÓN 2 DE LA FUENTE')
    print('-----------------------------------------------------------------')
    Calcular_L(8, 28, 10, 11, 2, LpRF2)
    Valores(LpRF2, 'dB')

    print()
    print('RUIDO DE FONDO EN HABITACIÓN SUPERIOR | POSICIÓN 3 DE LA FUENTE')
    print('-----------------------------------------------------------------')
    Calcular_L(8, 28, 13, 14, 2, LpRF3)
    Valores(LpRF3, 'dB')

    print()
    print('RUIDO DE FONDO EN HABITACIÓN SUPERIOR | POSICIÓN 4 DE LA FUENTE')
    print('-----------------------------------------------------------------')
    Calcular_L(8, 28, 16, 17, 2, LpRF4)
    Valores(LpRF4, 'dB')

    print()
    print('NIVELES CORREGIDOS EN RECEPCIÓN - HABITACIÓN | POSICIÓN 1 DE LA FUENTE')
    print('------------------------------------------------------------------------')
    print('Frecuencia | Lp Corregido Habitación')
    print('-------------------------------------')
    LCorregido(L_Impacto_F1, LpRF1, LpRC_F1)
    Valores(LpRC_F1, 'dB')

    print()
    print('NIVELES CORREGIDOS EN RECEPCIÓN - HABITACIÓN | POSICIÓN 2 DE LA FUENTE')
    print('-------------------------------------------------------------------------')
    print('Frecuencia | Lp Corregido Habitación')
    print('--------------------------------------')
    LCorregido(L_Impacto_F2, LpRF2, LpRC_F2)
    Valores(LpRC_F2, 'dB')

    print()
    print('NIVELES CORREGIDOS EN RECEPCIÓN - HABITACIÓN | POSICIÓN 3 DE LA FUENTE')
    print('-------------------------------------------------------------------------')
    print('Frecuencia | Lp Corregido Habitación')
    print('--------------------------------------')
    LCorregido(L_Impacto_F3, LpRF3, LpRC_F3)
    Valores(LpRC_F3, 'dB')

    print()
    print('NIVELES CORREGIDOS EN RECEPCIÓN - HABITACIÓN | POSICIÓN 4 DE LA FUENTE')
    print('------------------------------------------------------------------------')
    print('Frecuencia | Lp Corregido Habitación')
    print('--------------------------------------')
    LCorregido(L_Impacto_F4, LpRF4, LpRC_F4)
    Valores(LpRC_F4, 'dB')