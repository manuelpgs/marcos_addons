#!/usr/bin/env python2.7

SFSDEPT = 50

ESCALA_SALARIAL01 = 34685.00
SFS = 20
AFP = 30

# if 'SFSDEPT' in locals() or 'SFSDEPT' in globals():
#    DEDUCCIONES = SFS + AFP + SFSDEPT
# else:
#    DEDUCCIONES = SFS + AFP

DEDUCCIONES = SFS + AFP + SFSDEPT if 'SFSDEPT' in locals() or 'SFSDEPT' in globals() else SFS + AFP


print DEDUCCIONES
