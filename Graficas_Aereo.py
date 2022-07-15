# TFG Raquel Galán Montes
## Cálculo del Aislamiento a Ruido Aéreo  UNE-EN ISO 16283-1:2015 ISO 717-1:2013
### ESCALERAS, SALA COLINDANTE FRONTAL CON DIVISIÓN VERTICAL

from openpyxl import load_workbook      # Permite leer de ficheros .xlsx
import math                             # Permite usar funciones matemáticas
from pylab import *                     # Permite crear gráficas
from TR import *                        # Se importa el TR del programa
from Aereo_Escaleras import *           # Se importan los datos del Ruido Aéreo de las escaleras el TR del programa
from Aereo_Cocina import *              # Se importan los datos del Ruido Aéreo de la cocina
from Aereo_Salon import *               # Se importan los datos del Ruido Aéreo del salón
from Aereo_Hab_Sup import *             # Se importan los datos del Ruido Aéreo de la habitación superior
from Aereo_Hab_Inf import *             # Se importan los datos del Ruido Aéreo de la habitación inferior

# VARIABLES GLOBALES
SHEET = 'Datos'                 # Hoja del archivo XLSX
FILE  = 'Ruido_Aereo.xlsx'      # Variable para el fichero principal

## RANGO DE FRECUENCIAS
FR = ['50', '63', '80', '100', '125', '160', '200', '250', '315', '400', '500', '630', '800', '1000', '1250', '1600', '2000','2500', '3150', '4000', '5000']

DnT_F1=[]
DnT_F2=[]
DnT=[]
R_F1=[]
R_F2=[]
R=[]

## PROCEDIMIENTOS ESPECÍFICOS DE LA ISO 16283-1


# Datos mostrados en una gráfica
def Representacion_TR(A, B):
    title(A)
    xlabel('Frecuencia [Hz]')
    ylabel('Tiempo[s]')
    ylim(0, 1.5)
    legend((B),
    prop = {'size': 10}, loc='best')
    grid()

# Datos mostrados en una gráfica
def Representacion_Nivel(A, B):
    title(A)
    xlabel('Frecuencia [Hz]')
    ylabel('Niveles [dB]')
    ylim(0, 110)
    legend((B),
    prop = {'size': 10}, bbox_to_anchor=(1.05, 1.0), loc='best')
    grid()


# Se realizan los cálculos y se imprime por pantalla
if __name__ == "__main__":
    print()
    print('Tiempo de Reverberacion de la HABITACIÓN RECEPTORA')
    print('----------------------------------------------------')
    print('Frecuencia | TR')
    print('----------------------------------------------------')
    Calcular_TR(6, 26, 12, 15, TR_F1)
    Calcular_TR(6, 26, 19, 22, TR_F2)
    TR_Habitación(TR_F1, TR_F2, TR)
    Imprimir(TR, 's')

    #REPRESENTACIÓN DE TR
    figure("Tiempo de Reverberación de la Habitación")
    subplot(1,1,1)
    plot(FR, TR_F1, 'co-', TR_F2, 'bo-', TR, 'm*-')       # Genera el gráfico
    Representacion_TR('Tiempo de Reverberación TR20',
    ('TR_F1', 'TR_F2', 'TR'))

    # Cálculos de las ESCALERAS
    Calcular_Lp(33, 53, 4, 8, 5, LpR_Escaleras_F1)
    Calcular_Lp(33, 53, 9, 13, 5, LpR_Escaleras_F2)
    Calcular_Lp(139, 159, 5, 5, 1, LpRF_Escaleras)
    LpCorregido(LpR_Escaleras_F1, LpRF_Escaleras, LpRC_Escaleras_F1)
    LpCorregido(LpR_Escaleras_F2, LpRF_Escaleras, LpRC_Escaleras_F2)
    Calcular_Lp(33, 53, 17, 19, 3, LpE_Escaleras_F1)
    Calcular_Lp(33, 53, 20, 22, 3, LpE_Escaleras_F2)
    Diferencia_Nivel(LpE_Escaleras_F1, LpRC_Escaleras_F1, TR, DnT_F1_Escaleras)
    Diferencia_Nivel(LpE_Escaleras_F2, LpRC_Escaleras_F2, TR, DnT_F2_Escaleras)
    Sumatorio(DnT_F1_Escaleras, DnT_F2_Escaleras, DnT_Escaleras)
    Calcular_R(LpE_Escaleras_F1, LpRC_Escaleras_F1, TR, R_F1_Escaleras)
    Calcular_R(LpE_Escaleras_F2, LpRC_Escaleras_F2, TR, R_F2_Escaleras)
    Sumatorio(R_F1_Escaleras, R_F2_Escaleras, R_Escaleras)

    # Cálculos de la COCINA
    Calcular_Lp(61, 81, 4, 8, 5, LpR_Cocina_F1)
    Calcular_Lp(61, 81, 9, 13, 5, LpR_Cocina_F2)
    Calcular_Lp(139, 159, 6, 6, 1, LpRF_Cocina)
    LpCorregido(LpR_Cocina_F1, LpRF_Cocina, LpRC_Cocina_F1)
    LpCorregido(LpR_Cocina_F2, LpRF_Cocina, LpRC_Cocina_F2)
    Calcular_Lp(61, 81, 17, 19, 3, LpE_Cocina_F1)
    Calcular_Lp(61, 81, 20, 22, 3, LpE_Cocina_F2)
    Diferencia_Nivel(LpE_Cocina_F1, LpRC_Cocina_F1,TR, DnT_F1_Cocina)
    Diferencia_Nivel(LpE_Cocina_F2, LpRC_Cocina_F2, TR, DnT_F2_Cocina)
    Sumatorio(DnT_F1_Cocina, DnT_F2_Cocina, DnT_Cocina)
    Calcular_R(LpE_Cocina_F1, LpRC_Cocina_F1, TR, R_F1_Cocina)
    Calcular_R(LpE_Cocina_F2, LpRC_Cocina_F2, TR, R_F2_Cocina)
    Sumatorio(R_F1_Cocina, R_F2_Cocina, R_Cocina)

    # Cálculos del SALÓN
    Calcular_Lp(87, 107, 4, 8, 5, LpR_Salon_F1)
    Calcular_Lp(87, 107, 9, 13, 5, LpR_Salon_F2)
    Calcular_Lp(139, 159, 7, 7, 1, LpRF_Salon)
    LpCorregido(LpR_Salon_F1, LpRF_Salon, LpRC_Salon_F1)
    LpCorregido(LpR_Salon_F2, LpRF_Salon, LpRC_Salon_F2)
    Calcular_Lp(87, 107, 17, 21, 5, LpE_Salon_F1)
    Calcular_Lp(87, 107, 22, 26, 5, LpE_Salon_F2)
    Diferencia_Nivel(LpE_Salon_F1, LpRC_Salon_F1, TR, DnT_F1_Salon)
    Diferencia_Nivel(LpE_Salon_F2, LpRC_Salon_F2, TR, DnT_F2_Salon)
    Sumatorio(DnT_F1_Salon, DnT_F2_Salon, DnT_Salon)
    Calcular_R(LpE_Salon_F1, LpRC_Salon_F1, TR, R_F1_Salon)
    Calcular_R(LpE_Salon_F2, LpRC_Salon_F2, TR, R_F2_Salon)
    Sumatorio(R_F1_Salon, R_F2_Salon, R_Salon)

    # Cálculos de la HABITACIÓN SUPERIOR
    Calcular_Lp(6, 26, 4, 8, 5, LpR_Sup_F1)
    Calcular_Lp(6, 26, 9, 13, 5, LpR_Sup_F2)
    Calcular_Lp(139, 159, 4, 4, 1, LpRF_Sup)
    LpCorregido(LpR_Sup_F1, LpRF_Sup, LpRC_Sup_F1)
    LpCorregido(LpR_Sup_F2, LpRF_Sup, LpRC_Sup_F2)
    Calcular_Lp(6, 26, 17, 21, 5, LpE_Sup_F1)
    Calcular_Lp(6, 26, 22, 26, 5, LpE_Sup_F2)
    Diferencia_Nivel(LpE_Sup_F1, LpRC_Sup_F1, TR, DnT_F1_Sup)
    Diferencia_Nivel(LpE_Sup_F2, LpRC_Sup_F2, TR, DnT_F2_Sup)
    Sumatorio(DnT_F1_Sup, DnT_F2_Sup, DnT_Sup)
    Calcular_R(LpE_Sup_F1, LpRC_Sup_F1, TR, R_F1_Sup)
    Calcular_R(LpE_Sup_F2, LpRC_Sup_F2, TR, R_F2_Sup)
    Sumatorio(R_F1_Sup, R_F2_Sup, R_Sup)

    # Cálculos de la HABITACIÓN INFERIOR
    Calcular_Lp(113, 133, 4, 8, 5, LpR_Inf_F1)
    Calcular_Lp(113, 133, 9, 13, 5, LpR_Inf_F2)
    Calcular_Lp(139, 159, 8, 8, 1, LpRF_Inf)
    LpCorregido(LpR_Inf_F1, LpRF_Inf, LpRC_Inf_F1)
    LpCorregido(LpR_Inf_F2, LpRF_Inf, LpRC_Inf_F2)
    Calcular_Lp(113, 133, 17, 19, 3, LpE_Inf_F1)
    Calcular_Lp(113, 133, 20, 22, 3, LpE_Inf_F2)
    Diferencia_Nivel(LpE_Inf_F1, LpRC_Inf_F1, TR, DnT_F1_Inf)
    Diferencia_Nivel(LpE_Inf_F2, LpRC_Inf_F2, TR, DnT_F2_Inf)
    Sumatorio(DnT_F1_Inf, DnT_F2_Inf, DnT_Inf)
    Calcular_R(LpE_Inf_F1, LpRC_Inf_F1, TR, R_F1_Inf)
    Calcular_R(LpE_Inf_F2, LpRC_Inf_F2, TR, R_F2_Inf)
    Sumatorio(R_F1_Inf, R_F2_Inf, R_Inf)

    #REPRESENTACIÓN DE LOS NIVELES DE RECEPCIÓN
    figure("Niveles en recepción corregidos")
    plot(FR, LpRC_Escaleras_F1, 'bo-', LpRC_Escaleras_F1, 'bo-', LpRC_Cocina_F1, 'co-',
    LpRC_Cocina_F2, 'co-', LpRC_Salon_F1, 'yo-', LpRC_Salon_F2, 'yo-', 
    LpRC_Sup_F1, 'm*-', LpRC_Sup_F1, 'm*-', LpRC_Inf_F1, 'go-', LpRC_Inf_F2, 'go-')        # Genera el gráfico
    Representacion_Nivel('Diferencia estandarizada',
    ('LEscaleras_F1', 'LEscaleras_F2', 'LCocina_F1', 'LCocina_F2',
    'LSalon_F1', 'LSalon_F2', 'LSup_F1', 'LSup_F2', 'LInf_F1', 'LInf_F2'))

    #REPRESENTACIÓN DE DnT
    figure("Diferencia de Nivel Estandarizada DnT")
    plot(FR, DnT_Escaleras, 'bo-', DnT_Cocina, 'co-', DnT_Salon, 'yo-', DnT_Sup, 'm*-', DnT_Inf, 'go-')        # Genera el gráfico
    Representacion_Nivel('Diferencia estandarizada',
    ('DnT_Escaleras', 'DnT_Cocina', 'DnT_Salon', 'DnT_Hab_Superior', 'DnT_Hab_Inf'))

    #REPRESENTACIÓN DE R'
    figure("Índice de Reducción Aparente R'")
    plot(FR, R_Escaleras, 'bo-', R_Cocina, 'co-', R_Salon, 'yo-', R_Sup, 'm*-', R_Inf, 'go-')              # Genera el gráfico
    Representacion_Nivel('Índice de reducción sonora aparente',
    ("R'_Escaleras", "R'_Cocina", "R'_Salon", "R'_Hab_Superior", "R'_Hab_Inferior"))

    tight_layout()                                          # Ajusta la leyenda
    show()