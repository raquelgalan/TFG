# TFG Raquel Galán Montes
## Cálculo del Aislamiento a Ruido Aéreo en Baja Frecuencia UNE-EN ISO 16283-1:2015 ISO 717-1:2013
### El procedimiento de baja frecuencia se debe utilizar para las bandas de tercio de octava
### de 50 Hz, 63 Hz y 80 Hz en el recinto receptor cuando su volumen es inferior a 25 m3.

from openpyxl import load_workbook      # Nos permite leer de ficheros .xlsx
import math                             # Nos permite usar funciones matemáticas        
from Graficas_Aereo import *            # Importamos funciones del archivo donde se generan las gráficas
#from TR import *                        # Se importa el TR del programa

# Variables globales
SHEET = 'Datos'                         # Hoja del archivo XLSX
FILE  = 'Ruido_Aereo.xlsx'              # Variable para el fichero principal
FILE_Impactos = 'Ruido_Impactos.xlsx'   # Variable para el fichero principal
T = 0.5                                 # Tiempo de referencia = 0.5s
V = 23.4                        # Volumen del recinto receptor (V = largo x ancho x alto = 4.5 x 2.08 x 2.5 m^3)
S = 9.36                        # Superficie del elemento separador (S = techo = largo x ancho = 4.5 x 2.08 m^2)
C = 0.16                        # Constante para hallar Abs, la superficie de absorción equivalente
pos_mic = 4

# Arrays vacíos
# Escaleras
Lmax_Esc50F1 =[]
Lmax_Esc50F2 = []
Lmax_Esc63F1 = []
Lmax_Esc63F2 = []
Lmax_Esc80F1 = []
Lmax_Esc80F2 = []
Llf_Esc50_F1 = []
Llf_Esc50_F2 = []
Llf_Esc63_F1 = []
Llf_Esc63_F2 = []
Llf_Esc80_F1 = []
Llf_Esc80_F2 = []
LpR_Escaleras63_F1 =[]
LpR_Escaleras80_F1 = []
LpR_Escaleras63_F2 =[]
LpR_Escaleras80_F2 = []
# Salón
Lmax_Salon50F1 =[]
Lmax_Salon50F2 = []
Lmax_Salon63F1 = []
Lmax_Salon63F2 = []
Lmax_Salon80F1 = []
Lmax_Salon80F2 = []
Llf_Salon50_F1 = []
Llf_Salon50_F2 = []
Llf_Salon63_F1 = []
Llf_Salon63_F2 = []
Llf_Salon80_F1 = []
Llf_Salon80_F2 = []
LpR_Salon63_F1 =[]
LpR_Salon80_F1 = []
LpR_Salon63_F2 =[]
LpR_Salon80_F2 = []
# Cocina
Lmax_Cocina50F1 =[]
Lmax_Cocina50F2 = []
Lmax_Cocina63F1 = []
Lmax_Cocina63F2 = []
Lmax_Cocina80F1 = []
Lmax_Cocina80F2 = []
Llf_Cocina50_F1 = []
Llf_Cocina50_F2 = []
Llf_Cocina63_F1 = []
Llf_Cocina63_F2 = []
Llf_Cocina80_F1 = []
Llf_Cocina80_F2 = []
LpR_Cocina63_F1 =[]
LpR_Cocina80_F1 = []
LpR_Cocina63_F2 =[]
LpR_Cocina80_F2 = []
# Habitación Superior
Lmax_Sup50F1 =[]
Lmax_Sup50F2 = []
Lmax_Sup63F1 = []
Lmax_Sup63F2 = []
Lmax_Sup80F1 = []
Lmax_Sup80F2 = []
Llf_Sup50_F1 = []
Llf_Sup50_F2 = []
Llf_Sup63_F1 = []
Llf_Sup63_F2 = []
Llf_Sup80_F1 = []
Llf_Sup80_F2 = []
LpR_Sup63_F1 =[]
LpR_Sup80_F1 = []
LpR_Sup63_F2 =[]
LpR_Sup80_F2 = []
# Habitación Inferior
Lmax_Inf50F1 =[]
Lmax_Inf50F2 = []
Lmax_Inf63F1 = []
Lmax_Inf63F2 = []
Lmax_Inf80F1 = []
Lmax_Inf80F2 = []
Llf_Inf50_F1 = []
Llf_Inf50_F2 = []
Llf_Inf63_F1 = []
Llf_Inf63_F2 = []
Llf_Inf80_F1 = []
Llf_Inf80_F2 = []
LpR_Inf63_F1 =[]
LpR_Inf80_F1 = []
LpR_Inf63_F2 =[]
LpR_Inf80_F2 = []

# Rango de frecuencias de interes en baja frecuencia:
FR_baja = [50, 63, 80]

## PROCEDIMIENTO ESPECÍFICO DE LA ISO 16283-1 PARA BAJA FRECUENCIA
# Se preparan los resultados para imprimirlos por pantalla
def ResultadosBajaF(FR_baja, myArray, unidades):
    print(FR_baja, 'Hz - ', myArray, 'dB')        

# Se preparan los resultados para imprimirlos por pantalla
def PrintBajaF(myArray, unidades):
    i = 0                                             # Se inicializa el iterador de los arrays
    for num in FR_baja:
        print(FR_baja[i], 'Hz - ', myArray[i], 'dB')  # Se imprime por la terminal el elemento i del array
        i = i + 1                                     # Se va al siguiente elemento

# Cálculo del promedio de nivel de presión acústica para las posiciones de micrófono 
# segun el procedimiento de baja frecuencia de la ISO 16283-1:
def Calcular_Lbaja(A, B, myArray):
    Lbaja = (10**(A*0.1)) + 2*(10**(B*0.1))         # Se hace el cálculo según la norma
    Lbaja = 10*math.log(Lbaja/3, (10))
    myArray.append(round(Lbaja,1))                  # Array ordenado de datos

# Cálculos del RUIDO DE FONDO DEL RECEPTOR
Calcular_Lp(6, 8, 1, 1, 1, LpRF_Receptor)

#-----------------------------------------------------------------------
# ESCALERAS


print()
print('NIVELES EN RECEPCIÓN ESCALERAS en baja frecuencia - FUENTE 1')
print('--------------------------------------------------------------')
print('Frecuencia | Lp Escaleras')
print('---------------------------')
Calcular_Lp(200, 200, 5, 5, 1, Lmax_Esc50F1)
Lmax_Esc50F1 = Lmax_Esc50F1[0]
ResultadosBajaF(50, Lmax_Esc50F1, 'dB')
Calcular_Lp(201, 201, 7, 7, 1, Lmax_Esc63F1)
Lmax_Esc63F1 = Lmax_Esc63F1 [0]
ResultadosBajaF(63, Lmax_Esc63F1, 'dB')
Calcular_Lp(202, 202, 7, 7, 1, Lmax_Esc80F1)
Lmax_Esc80F1=Lmax_Esc80F1[0]
ResultadosBajaF(80, Lmax_Esc80F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN ESCALERAS en baja frecuencia - FUENTE 2')
print('--------------------------------------------------------------')
print('Frecuencia | Lp Escaleras')
print('---------------------------')
Calcular_Lp(200, 200, 9, 9, 1, Lmax_Esc50F2)
Lmax_Esc50F2 = Lmax_Esc50F2[0]
ResultadosBajaF(50, Lmax_Esc50F2, 'dB')
Calcular_Lp(201, 201, 11, 11, 1, Lmax_Esc63F2)
Lmax_Esc63F2=Lmax_Esc63F2[0]
ResultadosBajaF(63, Lmax_Esc63F2, 'dB')
Calcular_Lp(202, 202, 11, 11, 1, Lmax_Esc80F2)
Lmax_Esc80F2=Lmax_Esc80F2[0]
ResultadosBajaF(80, Lmax_Esc80F2, 'dB')

print()
print('NIVELES EN RECEPCIÓN ESCALERAS en media/alta frecuencia - FUENTE 1')
print('--------------------------------------------------------------------')
print('Frecuencia | Lp Escaleras')
print('---------------------------')
Calcular_Lp(33, 33, 4, 8, 5, LpR_Escaleras_F1)
LpR_Escaleras_F1 = LpR_Escaleras_F1[0]
ResultadosBajaF(50, LpR_Escaleras_F1, 'dB')

Calcular_Lp(34, 34, 4, 8, 5, LpR_Escaleras63_F1)
LpR_Escaleras63_F1 = LpR_Escaleras63_F1[0]
ResultadosBajaF(63, LpR_Escaleras63_F1, 'dB')

Calcular_Lp(35, 35, 4, 8, 5, LpR_Escaleras80_F1)
LpR_Escaleras80_F1 = LpR_Escaleras80_F1[0]
ResultadosBajaF(80, LpR_Escaleras80_F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN ESCALERAS en media/alta frecuencia - FUENTE 2')
print('--------------------------------------------------------------------')
print('Frecuencia | Lp Escaleras')
print('---------------------------')
Calcular_Lp(33, 33, 9, 13, 5, LpR_Escaleras_F2)
LpR_Escaleras_F2 = LpR_Escaleras_F2[0]
ResultadosBajaF(50, LpR_Escaleras_F2, 'dB')

Calcular_Lp(34, 34, 9, 13, 5, LpR_Escaleras63_F2)
LpR_Escaleras63_F2 = LpR_Escaleras63_F2[0]
ResultadosBajaF(63, LpR_Escaleras63_F2, 'dB')

Calcular_Lp(35, 35, 9, 13, 5, LpR_Escaleras80_F2)
LpR_Escaleras80_F2 = LpR_Escaleras80_F2[0]
ResultadosBajaF(80, LpR_Escaleras80_F2, 'dB')

print()
print('NIVELES PROMEDIADOS ESCALERAS en baja frecuencia - FUENTE 1')
print('--------------------------------------------------------------------')
print('Frecuencia | Lp Escaleras')
print('---------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Esc50F1, LpR_Escaleras_F1, Llf_Esc50_F1)
Llf_Esc50_F1 = Llf_Esc50_F1[0]
ResultadosBajaF(50, Llf_Esc50_F1, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Esc63F1, LpR_Escaleras63_F1, Llf_Esc63_F1)
Llf_Esc63_F1 = Llf_Esc63_F1[0]
ResultadosBajaF(63, Llf_Esc63_F1, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Esc80F1, LpR_Escaleras80_F1, Llf_Esc80_F1)
Llf_Esc80_F1 = Llf_Esc80_F1[0]
ResultadosBajaF(80, Llf_Esc80_F1, 'dB')

print()
print('NIVELES PROMEDIADOS ESCALERAS en baja frecuencia - FUENTE 2')
print('--------------------------------------------------------------------')
print('Frecuencia | Lp Escaleras')
print('---------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Esc50F2, LpR_Escaleras_F2, Llf_Esc50_F2)
Llf_Esc50_F2 = Llf_Esc50_F2[0]
ResultadosBajaF(50, Llf_Esc50_F2, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Esc63F2, LpR_Escaleras63_F2, Llf_Esc63_F2)
Llf_Esc63_F2 = Llf_Esc63_F2[0]
ResultadosBajaF(63, Llf_Esc63_F2, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Esc80F2, LpR_Escaleras80_F2, Llf_Esc80_F2)
Llf_Esc80_F2 = Llf_Esc80_F2[0]
ResultadosBajaF(80, Llf_Esc80_F2, 'dB')

#-----------------------------------------------------------------------
# SALÓN

Resultados(LpRF_Salon, 'dB')

print()
print('NIVELES EN RECEPCIÓN SALÓN en baja frecuencia - FUENTE 1')
print('--------------------------------------------------------------')
print('Frecuencia | Lp Salón')
print('---------------------------')
Calcular_Lp(218, 218, 7, 7, 1, Lmax_Salon50F1)
Lmax_Salon50F1 = Lmax_Salon50F1[0]
ResultadosBajaF(50, Lmax_Salon50F1, 'dB')
Calcular_Lp(219, 219, 5, 5, 1, Lmax_Salon63F1)
Lmax_Salon63F1 = Lmax_Salon63F1 [0]
ResultadosBajaF(63, Lmax_Salon63F1, 'dB')
Calcular_Lp(220, 220, 7, 7, 1, Lmax_Salon80F1)
Lmax_Salon80F1=Lmax_Salon80F1[0]
ResultadosBajaF(80, Lmax_Salon80F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN SALÓN en baja frecuencia - FUENTE 2')
print('--------------------------------------------------------------')
print('Frecuencia | Lp Salón')
print('---------------------------')
Calcular_Lp(218, 218, 11, 11, 1, Lmax_Salon50F2)
Lmax_Salon50F2 = Lmax_Salon50F2[0]
ResultadosBajaF(50, Lmax_Salon50F2, 'dB')
Calcular_Lp(219, 219, 9, 9, 1, Lmax_Salon63F2)
Lmax_Salon63F2=Lmax_Salon63F2[0]
ResultadosBajaF(63, Lmax_Salon63F2, 'dB')
Calcular_Lp(220, 220, 11, 11, 1, Lmax_Salon80F2)
Lmax_Salon80F2=Lmax_Salon80F2[0]
ResultadosBajaF(80, Lmax_Salon80F2, 'dB')

print()
print('NIVELES EN RECEPCIÓN SALÓN en media/alta frecuencia - FUENTE 1')
print('--------------------------------------------------------------------')
print('Frecuencia | Lp Salón')
print('---------------------------')
Calcular_Lp(87, 87, 4, 8, 5, LpR_Salon_F1)
LpR_Salon_F1 = LpR_Salon_F1[0]
ResultadosBajaF(50, LpR_Salon_F1, 'dB')

Calcular_Lp(88, 88, 4, 8, 5, LpR_Salon63_F1)
LpR_Salon63_F1 = LpR_Salon63_F1[0]
ResultadosBajaF(63, LpR_Salon63_F1, 'dB')

Calcular_Lp(89, 89, 4, 8, 5, LpR_Salon80_F1)
LpR_Salon80_F1 = LpR_Salon80_F1[0]
ResultadosBajaF(80, LpR_Salon80_F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN SALÓN en media/alta frecuencia - FUENTE 2')
print('--------------------------------------------------------------------')
print('Frecuencia | Lp Salón')
print('---------------------------')
Calcular_Lp(87, 87, 9, 13, 5, LpR_Salon_F2)
LpR_Salon_F2 = LpR_Salon_F2[0]
ResultadosBajaF(50, LpR_Salon_F2, 'dB')

Calcular_Lp(88, 88, 9, 13, 5, LpR_Salon63_F2)
LpR_Salon63_F2 = LpR_Salon63_F2[0]
ResultadosBajaF(63, LpR_Salon63_F2, 'dB')

Calcular_Lp(89, 89, 9, 13, 5, LpR_Salon80_F2)
LpR_Salon80_F2 = LpR_Salon80_F2[0]
ResultadosBajaF(80, LpR_Salon80_F2, 'dB')

print()
print('NIVELES PROMEDIADOS SALÓN en baja frecuencia - FUENTE 1')
print('---------------------------------------------------------')
print('Frecuencia | Lp Salón')
print('-----------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Salon50F1, LpR_Salon_F1, Llf_Salon50_F1)
Llf_Salon50_F1 = Llf_Salon50_F1[0]
ResultadosBajaF(50, Llf_Salon50_F1, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Salon63F1, LpR_Salon63_F1, Llf_Salon63_F1)
Llf_Salon63_F1 = Llf_Salon63_F1[0]
ResultadosBajaF(63, Llf_Salon63_F1, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Salon80F1, LpR_Salon80_F1, Llf_Salon80_F1)
Llf_Salon80_F1 = Llf_Salon80_F1[0]
ResultadosBajaF(80, Llf_Salon80_F1, 'dB')

print()
print('NIVELES PROMEDIADOS SALÓN en baja frecuencia - FUENTE 2')
print('---------------------------------------------------------')
print('Frecuencia | Lp Salón')
print('-----------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Salon50F2, LpR_Salon_F2, Llf_Salon50_F2)
Llf_Salon50_F2 = Llf_Salon50_F2[0]
ResultadosBajaF(50, Llf_Salon50_F2, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Salon63F2, LpR_Salon63_F2, Llf_Salon63_F2)
Llf_Salon63_F2 = Llf_Salon63_F2[0]
ResultadosBajaF(63, Llf_Salon63_F2, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Salon80F2, LpR_Salon80_F2, Llf_Salon80_F2)
Llf_Salon80_F2 = Llf_Salon80_F2[0]
ResultadosBajaF(80, Llf_Salon80_F2, 'dB')

#-----------------------------------------------------------------------
# COCINA
print()
print('NIVELES EN RECEPCIÓN COCINA en baja frecuencia - FUENTE 1')
print('-----------------------------------------------------------')
print('Frecuencia | Lp Cocina')
print('------------------------')
Calcular_Lp(209, 209, 5, 5, 1, Lmax_Cocina50F1)
Lmax_Cocina50F1 = Lmax_Cocina50F1[0]
ResultadosBajaF(50, Lmax_Cocina50F1, 'dB')
Calcular_Lp(210, 210, 5, 5, 1, Lmax_Cocina63F1)
Lmax_Cocina63F1 = Lmax_Cocina63F1 [0]
ResultadosBajaF(63, Lmax_Cocina63F1, 'dB')
Calcular_Lp(211, 211, 5, 5, 1, Lmax_Cocina80F1)
Lmax_Cocina80F1=Lmax_Cocina80F1[0]
ResultadosBajaF(80, Lmax_Cocina80F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN COCINA en baja frecuencia - FUENTE 2')
print('-----------------------------------------------------------')
print('Frecuencia | Lp Cocina')
print('------------------------')
Calcular_Lp(209, 209, 9, 9, 1, Lmax_Cocina50F2)
Lmax_Cocina50F2 = Lmax_Cocina50F2[0]
ResultadosBajaF(50, Lmax_Cocina50F2, 'dB')
Calcular_Lp(210, 210, 9, 9, 1, Lmax_Cocina63F2)
Lmax_Cocina63F2=Lmax_Cocina63F2[0]
ResultadosBajaF(63, Lmax_Cocina63F2, 'dB')
Calcular_Lp(211, 211, 11, 11, 1, Lmax_Cocina80F2)
Lmax_Cocina80F2=Lmax_Cocina80F2[0]
ResultadosBajaF(80, Lmax_Cocina80F2, 'dB')

print()
print('NIVELES EN RECEPCIÓN COCINA en media/alta frecuencia - FUENTE 1')
print('-----------------------------------------------------------------')
print('Frecuencia | Lp Cocina')
print('------------------------')
Calcular_Lp(61, 61, 4, 8, 5, LpR_Cocina_F1)
LpR_Cocina_F1 = LpR_Cocina_F1[0]
ResultadosBajaF(50, LpR_Cocina_F1, 'dB')

Calcular_Lp(62, 62, 4, 8, 5, LpR_Cocina63_F1)
LpR_Cocina63_F1 = LpR_Cocina63_F1[0]
ResultadosBajaF(63, LpR_Cocina63_F1, 'dB')

Calcular_Lp(63, 63, 4, 8, 5, LpR_Cocina80_F1)
LpR_Cocina80_F1 = LpR_Cocina80_F1[0]
ResultadosBajaF(80, LpR_Cocina80_F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN COCINA en media/alta frecuencia - FUENTE 2')
print('-----------------------------------------------------------------')
print('Frecuencia | Lp Cocina')
print('------------------------')
Calcular_Lp(61, 61, 9, 13, 5, LpR_Cocina_F2)
LpR_Cocina_F2 = LpR_Cocina_F2[0]
ResultadosBajaF(50, LpR_Cocina_F2, 'dB')

Calcular_Lp(62, 62, 9, 13, 5, LpR_Cocina63_F2)
LpR_Cocina63_F2 = LpR_Cocina63_F2[0]
ResultadosBajaF(63, LpR_Cocina63_F2, 'dB')

Calcular_Lp(63, 63, 9, 13, 5, LpR_Cocina80_F2)
LpR_Cocina80_F2 = LpR_Cocina80_F2[0]
ResultadosBajaF(80, LpR_Cocina80_F2, 'dB')

print()
print('NIVELES PROMEDIADOS COCINA en baja frecuencia - FUENTE 1')
print('-----------------------------------------------------------')
print('Frecuencia | Lp Cocina')
print('------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Cocina50F1, LpR_Cocina_F1, Llf_Cocina50_F1)
Llf_Cocina50_F1 = Llf_Cocina50_F1[0]
ResultadosBajaF(50, Llf_Cocina50_F1, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Cocina63F1, LpR_Cocina63_F1, Llf_Cocina63_F1)
Llf_Cocina63_F1 = Llf_Cocina63_F1[0]
ResultadosBajaF(63, Llf_Cocina63_F1, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Cocina80F1, LpR_Cocina80_F1, Llf_Cocina80_F1)
Llf_Cocina80_F1 = Llf_Cocina80_F1[0]
ResultadosBajaF(80, Llf_Cocina80_F1, 'dB')

print()
print('NIVELES PROMEDIADOS COCINA en baja frecuencia - FUENTE 2')
print('----------------------------------------------------------')
print('Frecuencia | Lp Cocina')
print('------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Cocina50F2, LpR_Cocina_F2, Llf_Cocina50_F2)
Llf_Cocina50_F2 = Llf_Cocina50_F2[0]
ResultadosBajaF(50, Llf_Cocina50_F2, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Cocina63F2, LpR_Cocina63_F2, Llf_Cocina63_F2)
Llf_Cocina63_F2 = Llf_Cocina63_F2[0]
ResultadosBajaF(63, Llf_Cocina63_F2, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Cocina80F2, LpR_Cocina80_F2, Llf_Cocina80_F2)
Llf_Cocina80_F2 = Llf_Cocina80_F2[0]
ResultadosBajaF(80, Llf_Cocina80_F2, 'dB')
#-----------------------------------------------------------------------
# HABITACIÓN SUPERIOR
print()
print('NIVELES EN RECEPCIÓN HABITACIÓN SUPERIOR en baja frecuencia - FUENTE 1')
print('------------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Superior')
print('-------------------------------------')
Calcular_Lp(191, 191, 5, 5, 1, Lmax_Sup50F1)
Lmax_Sup50F1 = Lmax_Sup50F1[0]
ResultadosBajaF(50, Lmax_Sup50F1, 'dB')
Calcular_Lp(192, 192, 5, 5, 1, Lmax_Sup63F1)
Lmax_Sup63F1 = Lmax_Sup63F1 [0]
ResultadosBajaF(63, Lmax_Sup63F1, 'dB')
Calcular_Lp(193, 193, 7, 7, 1, Lmax_Sup80F1)
Lmax_Sup80F1=Lmax_Sup80F1[0]
ResultadosBajaF(80, Lmax_Sup80F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN HABITACIÓN SUPERIOR en baja frecuencia - FUENTE 2')
print('-------------------------------------------------------------------------')
print('Frecuencia | Lp Sup')
print('---------------------')
Calcular_Lp(191, 191, 9, 9, 1, Lmax_Sup50F2)
Lmax_Sup50F2 = Lmax_Sup50F2[0]
ResultadosBajaF(50, Lmax_Sup50F2, 'dB')
Calcular_Lp(192, 192, 9, 9, 1, Lmax_Sup63F2)
Lmax_Sup63F2=Lmax_Sup63F2[0]
ResultadosBajaF(63, Lmax_Sup63F2, 'dB')
Calcular_Lp(193, 193, 9, 9, 1, Lmax_Sup80F2)
Lmax_Sup80F2=Lmax_Sup80F2[0]
ResultadosBajaF(80, Lmax_Sup80F2, 'dB')

print()
print('NIVELES EN RECEPCIÓN HABITACIÓN SUPERIOR en media/alta frecuencia - FUENTE 1')
print('-------------------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Superior')
print('-------------------------------------')
Calcular_Lp(6, 6, 4, 8, 5, LpR_Sup_F1)
LpR_Sup_F1 = LpR_Sup_F1[0]
ResultadosBajaF(50, LpR_Sup_F1, 'dB')

Calcular_Lp(7, 7, 4, 8, 5, LpR_Sup63_F1)
LpR_Sup63_F1 = LpR_Sup63_F1[0]
ResultadosBajaF(63, LpR_Sup63_F1, 'dB')

Calcular_Lp(8, 8, 4, 8, 5, LpR_Sup80_F1)
LpR_Sup80_F1 = LpR_Sup80_F1[0]
ResultadosBajaF(80, LpR_Sup80_F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN HABITACIÓN SUPERIOR en media/alta frecuencia - FUENTE 2')
print('------------------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Superior')
print('-------------------------------------')
Calcular_Lp(6, 6, 9, 13, 5, LpR_Sup_F2)
LpR_Sup_F2 = LpR_Sup_F2[0]
ResultadosBajaF(50, LpR_Sup_F2, 'dB')

Calcular_Lp(7, 7, 9, 13, 5, LpR_Sup63_F2)
LpR_Sup63_F2 = LpR_Sup63_F2[0]
ResultadosBajaF(63, LpR_Sup63_F2, 'dB')

Calcular_Lp(8, 8, 9, 13, 5, LpR_Sup80_F2)
LpR_Sup80_F2 = LpR_Sup80_F2[0]
ResultadosBajaF(80, LpR_Sup80_F2, 'dB')

print()
print('NIVELES PROMEDIADOS HABITACIÓN SUPERIOR en baja frecuencia - FUENTE 1')
print('------------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Superior')
print('-------------------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Sup50F1, LpR_Sup_F1, Llf_Sup50_F1)
Llf_Sup50_F1 = Llf_Sup50_F1[0]
ResultadosBajaF(50, Llf_Sup50_F1, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Sup63F1, LpR_Sup63_F1, Llf_Sup63_F1)
Llf_Sup63_F1 = Llf_Sup63_F1[0]
ResultadosBajaF(63, Llf_Sup63_F1, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Sup80F1, LpR_Sup80_F1, Llf_Sup80_F1)
Llf_Sup80_F1 = Llf_Sup80_F1[0]
ResultadosBajaF(80, Llf_Sup80_F1, 'dB')

print()
print('NIVELES PROMEDIADOS HABITACIÓN SUPERIOR en baja frecuencia - FUENTE 2')
print('-----------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Superior')
print('-------------------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Sup50F2, LpR_Sup_F2, Llf_Sup50_F2)
Llf_Sup50_F2 = Llf_Sup50_F2[0]
ResultadosBajaF(50, Llf_Sup50_F2, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Sup63F2, LpR_Sup63_F2, Llf_Sup63_F2)
Llf_Sup63_F2 = Llf_Sup63_F2[0]
ResultadosBajaF(63, Llf_Sup63_F2, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Sup80F2, LpR_Sup80_F2, Llf_Sup80_F2)
Llf_Sup80_F2 = Llf_Sup80_F2[0]
ResultadosBajaF(80, Llf_Sup80_F2, 'dB')

#-----------------------------------------------------------------------
# HABITACIÓN INFERIOR
print()
print('NIVELES EN RECEPCIÓN HABITACIÓN INFERIOR en baja frecuencia - FUENTE 1')
print('------------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Inferior')
print('-------------------------------------')
Calcular_Lp(227, 227, 7, 7, 1, Lmax_Inf50F1)
Lmax_Inf50F1 = Lmax_Inf50F1[0]
ResultadosBajaF(50, Lmax_Inf50F1, 'dB')
Calcular_Lp(228, 228, 5, 5, 1, Lmax_Inf63F1)
Lmax_Inf63F1 = Lmax_Inf63F1 [0]
ResultadosBajaF(63, Lmax_Inf63F1, 'dB')
Calcular_Lp(229, 229, 7, 7, 1, Lmax_Inf80F1)
Lmax_Inf80F1=Lmax_Inf80F1[0]
ResultadosBajaF(80, Lmax_Inf80F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN HABITACIÓN INFERIOR en baja frecuencia - FUENTE 2')
print('------------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Inferior')
print('-------------------------------------')
Calcular_Lp(227, 227, 11, 11, 1, Lmax_Inf50F2)
Lmax_Inf50F2 = Lmax_Inf50F2[0]
ResultadosBajaF(50, Lmax_Inf50F2, 'dB')
Calcular_Lp(228, 228, 11, 11, 1, Lmax_Inf63F2)
Lmax_Inf63F2=Lmax_Inf63F2[0]
ResultadosBajaF(63, Lmax_Inf63F2, 'dB')
Calcular_Lp(229, 229, 9, 9, 1, Lmax_Inf80F2)
Lmax_Inf80F2=Lmax_Inf80F2[0]
ResultadosBajaF(80, Lmax_Inf80F2, 'dB')

print()
print('NIVELES EN RECEPCIÓN HABITACIÓN INFERIOR en media/alta frecuencia - FUENTE 1')
print('------------------------------------------------------------------------------')
print('Frecuencia | Lp Habitacion Inferior')
print('-------------------------------------')
Calcular_Lp(113, 113, 4, 8, 5, LpR_Inf_F1)
LpR_Inf_F1 = LpR_Inf_F1[0]
ResultadosBajaF(50, LpR_Inf_F1, 'dB')

Calcular_Lp(114, 114, 4, 8, 5, LpR_Inf63_F1)
LpR_Inf63_F1 = LpR_Inf63_F1[0]
ResultadosBajaF(63, LpR_Inf63_F1, 'dB')

Calcular_Lp(115, 115, 4, 8, 5, LpR_Inf80_F1)
LpR_Inf80_F1 = LpR_Inf80_F1[0]
ResultadosBajaF(80, LpR_Inf80_F1, 'dB')

print()
print('NIVELES EN RECEPCIÓN HABITACIÓN INFERIOR en media/alta frecuencia - FUENTE 2')
print('------------------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Inferior')
print('--------------------------------------')
Calcular_Lp(113, 113, 9, 13, 5, LpR_Inf_F2)
LpR_Inf_F2 = LpR_Inf_F2[0]
ResultadosBajaF(50, LpR_Inf_F2, 'dB')

Calcular_Lp(114, 114, 9, 13, 5, LpR_Inf63_F2)
LpR_Inf63_F2 = LpR_Inf63_F2[0]
ResultadosBajaF(63, LpR_Inf63_F2, 'dB')

Calcular_Lp(115, 115, 9, 13, 5, LpR_Inf80_F2)
LpR_Inf80_F2 = LpR_Inf80_F2[0]
ResultadosBajaF(80, LpR_Inf80_F2, 'dB')

print()
print('NIVELES PROMEDIADOS HABITACIÓN INFERIOR en baja frecuencia - FUENTE 1')
print('-----------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Inferior')
print('-------------------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Inf50F1, LpR_Inf_F1, Llf_Inf50_F1)
Llf_Inf50_F1 = Llf_Inf50_F1[0]
ResultadosBajaF(50, Llf_Inf50_F1, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Inf63F1, LpR_Inf63_F1, Llf_Inf63_F1)
Llf_Inf63_F1 = Llf_Inf63_F1[0]
ResultadosBajaF(63, Llf_Inf63_F1, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Inf80F1, LpR_Inf80_F1, Llf_Inf80_F1)
Llf_Inf80_F1 = Llf_Inf80_F1[0]
ResultadosBajaF(80, Llf_Inf80_F1, 'dB')

print()
print('NIVELES PROMEDIADOS HABITACIÓN INFERIOR en baja frecuencia - FUENTE 2')
print('-----------------------------------------------------------------------')
print('Frecuencia | Lp Habitación Inferior')
print('--------------------------------------')
# 50 Hz
Calcular_Lbaja(Lmax_Inf50F2, LpR_Inf_F2, Llf_Inf50_F2)
Llf_Inf50_F2 = Llf_Inf50_F2[0]
ResultadosBajaF(50, Llf_Inf50_F2, 'dB')
# 63 Hz
Calcular_Lbaja(Lmax_Inf63F2, LpR_Inf63_F2, Llf_Inf63_F2)
Llf_Inf63_F2 = Llf_Inf63_F2[0]
ResultadosBajaF(63, Llf_Inf63_F2, 'dB')
# 80 Hz
Calcular_Lbaja(Lmax_Inf80F2, LpR_Inf80_F2, Llf_Inf80_F2)
Llf_Inf80_F2 = Llf_Inf80_F2[0]
ResultadosBajaF(80, Llf_Inf80_F2, 'dB')


# Cálculo de la diferencia estandarizada para cada banda de frecuencia, DnT:
# A representa el Lp en el recinto EMISOR y B el Lp en el recinto RECEPTOR.
def Diferencia_Nivel(A, B, TR, myArray):
    i = 0
    for num in A:
        diferencia = A[i] - B[i]
        DnT = diferencia + (10*math.log(TR[i]/T,10))
        i = i + 1
        myArray.append(round(DnT,1))

        print('DnT(' + FR + 'Hz) = ', round(DnT,1), 'dB')   # Imprimo en el terminal el resultado
        return(DnT)