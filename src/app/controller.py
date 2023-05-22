from src.app.model import *
from src.app.util import *
from src.app.entity import *

class CategoriacController:
    def __init__(self) :
        self.__model=Operaciones()
        
    
    def procesarA(self,pe): #pe es un objeto de la clase Calculadora
        self.__model.categoriaA(pe)
        self.__resultado1=TITULO+'\n'+RAYA+\
                    '\nsueldoBas: '+str(pe.sueldoBas)+\
                    '\ndescuentoTar: '+str(pe.descuentoTar)+\
                    '\npxhe: '+str(pe.pxhe)+\
                    '\nsueldoNeto: '+str(pe.sueldoNeto)\
                        
        return self.__resultado1
    
    def procesarB(self,pe): #pe es un objeto de la clase Calculadora
        self.__model.categoriaB(pe)
        self.__resultado2=TITULO+'\n'+RAYA+\
                    '\nsueldoBas: '+str(pe.sueldoBas)+\
                    '\ndescuentoTar: '+str(pe.descuentoTar)+\
                    '\npxhe: '+str(pe.pxhe)+\
                    '\nsueldoNeto: '+str(pe.sueldoNeto)\
                        
        return self.__resultado2
    
    def procesarC(self,pe): #pe es un objeto de la clase Calculadora
        self.__model.categoriaC(pe)
        self.__resultado3=TITULO+'\n'+RAYA+\
                    '\nsueldoBas: '+str(pe.sueldoBas)+\
                    '\ndescuentoTar: '+str(pe.descuentoTar)+\
                    '\npxhe: '+str(pe.pxhe)+\
                    '\nsueldoNeto: '+str(pe.sueldoNeto)\
                        
        return self.__resultado3