from src.app.controller import *
from src.app.model import *
from src.app.util import *
from src.app.entity import *

class prueba:
    trabajador=input("ingrese nombre del trabajador: ")
    categoria=input("ingrese la categoria del trabajador: ")
    he=float(input("ingrese horas extras: "))
    tardanzas=float(input("ingrese tardanzas en (MINUTOS): "))
    
    pe= Datos(trabajador,categoria,he,tardanzas)
    
    obj=categoriacController()
    
    resultado1=obj.procesarA(pe)
    resultado2=obj.procesarB(pe)
    resultado3=obj.procesarC(pe)
    
    if categoria == 'A':
        print(resultado1)
    elif categoria == 'B':
        print(resultado2)
    elif categoria == 'C':
        print(resultado3)