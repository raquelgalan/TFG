# TFG Raquel Galán Montes
## Cálculo del Aislamiento a Ruido Aéreo  UNE-EN ISO 16283-1:2015 ISO 717-1:2013
### HABITACIÓN SUPERIOR

from openpyxl import load_workbook      # Nos permite leer de ficheros .xlsx
import math                             # Nos permite usar funciones matemáticas
from pylab import *                     # Nos permite crear gráficos
from TR import *                        # Importamos el TR del programa

# VARIABLES GLOBALES
SHEET = 'Datos'                 # Hoja del archivo XLSX
FILE  = 'Ruido_Aereo.xlsx'      # Variable para el fichero principal
#FILE_TR = 'TR.xlsx'             # Variable para un segundo fichero (TR)
T = 0.5                         # Tiempo de referencia = 0.5s
V = 23.4                        # Volumen del recinto receptor


# Rango de frecuencias de interes:
arrayFR = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000]

# Arrays vacíos
LpE_Sup_F1 = []           # Array para los resultados del nivel de presión en emisión , LpE-Sup-F1
LpE_Sup_F2 = []           # Array para los resultados del nivel de presión en emisión , LpE-Sup-F2
LpEC_Sup_F1 = []           # Array para los resultados del nivel de presión en emisión , LpEC-Sup-F1
LpEC_Sup_F2 = []           # Array para los resultados del nivel de presión en emisión , LpEC-Sup-F2
LpECor_Sup_F1 = []           # Array para los resultados del nivel de presión en emisión , LpEC-Sup-F1
LpECor_Sup_F2 = []           # Array para los resultados del nivel de presión en emisión , LpEC-Sup-F2
LpRF = []
LpE_Inf = []           # Array para los resultados del nivel de presión en emisión , LpE-Inf
LpE_Cocina = []        # Array para los resultados del nivel de presión en emisión , LpE-Cocina
LpE_Salon = []         # Array para los resultados del nivel de presión en emisión , LpE-Salon
LpE_Esc = []           # Array para los resultados del nivel de presión en emisión , LpE-Esc
LpR = []               # Array para los resultados del nivel de presión en recepción, LpR
TR = []                # Array para los resultados del tiempo de reverberación en recepción, TR
DnT_A1 = []            # Array para los resultados del nivel de diferencia normalizada, DnT-A1
DnT_A2 = []            # Array para los resultados del nivel de diferencia normalizada, DnT-A2
myDnT = []             # Array para los resultados del nivel de diferencia normalizada global, DnT
R_A1 = []              # Array para los resultados del índice de reducción sonora aparente, R'- A1
R_A2 = []              # Array para los resultados del índice de reducción sonora aparente, R'- A2
myR = []               # Array para los resultados del índice de reducción sonora aparente global, R'

## PROCEDIMIENTOS ESPECÍFICOS DE LA ISO 16283-1
# Cálculo del promedio de posiciones de micrófono para cada banda de frecuencia, Lp, donde
# A: min_row; B: max_row; C: min_col; D: max_col; n: posiciones de micrófono
def Calcular_Lp(A, B, C, D, n, myArray):
    wb = load_workbook(FILE)        # Cargamos en wb el fichero
    sheet = wb[SHEET]               # Cargamos la hoja del fichero de donde obtenemos los datos

    for value in sheet.iter_rows(min_row =A, max_row =B, min_col = C, max_col =D,
                                 values_only=True):
        i = 0
        L = 0
        for cell in value:
            L = L + 10**(value[i]/10)       # calculo 10*(Lp/10) y sumo al resultado anterior.
            i = i + 1
        L = 10*math.log(L/n,(10))      # Calculo el promedio logaritmico de la suma total, L.
        myArray.append(round(L,1))          # Array ordenado de datos

# Diferencia del nivel de ruido de fondo:
def Ldif(A, B, myArray):
    i = 0
    h = 10
    l = 6
    correccion = 1.3
    for num in A:
        dif = A[i] - B[i]

        if dif > h:
            corregido = A[i]
            myArray.append(round(corregido,2))
            #print ("Ldif > 10")
            i = i + 1
        elif dif < l:
            corregido = A[i] - l
            myArray.append(round(corregido,2))
            print ("Ldif < 6")
            i = i + 1

        else:
            corregido = 10*math.log(10**(A[i]/10)-10**(B[i]/10))   
            myArray.append(round(corregido,2))
            print ("Ldif < 10")
            i = i + 1

       # myArray.append(round(dif))

# Corrección del ruido de fondo:
def LpCorregido(A, B, myArray):

    l = 6
    cor = 1.3
    h = 10
    i = 0
    for num in A:
        if Ldif > h:
            corregido = A[i] - B[i]
            i = i + 1
            print ("Ldif > 10")
            print  (corregido)

        elif Ldif < l:
            corregido = Ldif - cor
            myArray.append(round(corregido))
            print ("Ldif < 3" + corregido)

        else:

            print ("Ldif > 3 y < 10" )



# Cálculo del sumatorio de las magnitudes en función de la posición de altavoz:
# donde A y B son los resultados por cada posición de altavoz respectivamente para cada banda de frecuencias.
def toSum(A, B, myArray):
    i = 0
    for num in A:
        sum = 10**(-A[i]/10) + 10**(-B[i]/10)       # Hacemos el cálculo como indica la norma
        X = -10*math.log(sum/2,(10))                # Dividimos entre 2, el número de posiciones de altavoz, A1 y A2
        i = i + 1
        myArray.append(round(X,1))


# Se preparan los resultados para imprimirlos por pantalla
def Imprimir(myArray, unidades):
    i = 0                                             # Iterador para los arrays
    for num in arrayFR:
        print(arrayFR[i], 'Hz - ', myArray[i], 'dB')  # Se imprime por la terminal el elemento i del array
        i = i + 1                                     # Siguiente elemento


if __name__ == "__main__":
    print()
    print('NIVELES EN EMISIÓN HABITACIÓN SUPERIOR - FUENTE 1')
    print('----------------------------------------')
    print('Frecuencia | Lp Hab. Superior')
    print('----------------------------------------')
    Calcular_Lp(6, 26, 4, 8, 5, LpE_Sup_F1)
    Imprimir(LpE_Sup_F1, 'dB')

    print()
    print('NIVELES EN EMISIÓN HABITACIÓN SUPERIOR - FUENTE 2')
    print('----------------------------------------')
    print('Frecuencia | Lp Hab. SUPERIOR')
    print('----------------------------------------')
    Calcular_Lp(6, 26, 9, 13, 5, LpE_Sup_F2)
    Imprimir(LpE_Sup_F2, 'dB')
    
    print()
    print('RUIDO DE FONDO EN HABITACIÓN SUPERIOR')
    print('--------------------')
    Calcular_Lp(139, 159, 4, 4, 1, LpRF)
    Imprimir(LpRF, 'dB')

    print()
    print('NIVELES CORREGIDOS EN EMISIÓN - HABITACIÓN SUPERIOR - FUENTE 1')
    print('----------------------------------------')
    print('Frecuencia | Lp Corregido Hab. Superior')
    print('----------------------------------------')
    Ldif(LpE_Sup_F1, LpRF, LpEC_Sup_F1)
    Imprimir(LpEC_Sup_F1, 'dB')

    print()
    print('NIVELES CORREGIDOS EN EMISIÓN - HABITACIÓN SUPERIOR - FUENTE 2')
    print('----------------------------------------')
    print('Frecuencia | Lp Corregido Hab. Superior')
    print('----------------------------------------')
    Ldif(LpE_Sup_F2, LpRF, LpEC_Sup_F2)
    Imprimir(LpEC_Sup_F2, 'dB')

    print()
    print('NIVELES CORREGIDOS EN EMISIÓN - HABITACIÓN INFERIOR - FUENTE 1')
    print('----------------------------------------')
    print('Frecuencia | Lp Corregido Hab. Inferior')
    print('----------------------------------------')
    Ldif(LpE_Sup_F1, LpRF, LpEC_Sup_F1)
    Imprimir(LpEC_Sup_F1, 'dB')

    print()
    print('NIVELES CORREGIDOS EN EMISIÓN - HABITACIÓN INFERIOR - FUENTE 2')
    print('----------------------------------------')
    print('Frecuencia | Lp Corregido Hab. Inferior')
    print('----------------------------------------')
    Ldif(LpE_Sup_F2, LpRF, LpEC_Sup_F2)
    Imprimir(LpEC_Sup_F2, 'dB')