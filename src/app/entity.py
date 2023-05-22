class Datos:
    def __init__(self,trabajador,categoria,he,tardanzas):
        self.__trabajador=trabajador
        self.__categoria=categoria
        self.__he=he
        self.__tardanzas=tardanzas
        self.__sueldoBas=0
        self.__descuentoTar=0
        self.__pxhe=0
        self.__sueldoNeto=0
        self.__pagoxhora=0
        self.__categoria=''
        self.__newcategoria=0
    
    @property
    def trabajador(self):
        return self.__trabajador 
    @property
    def categoria(self):
        return self.__categoria 
    @property
    def he(self):
        return self.__he 
    @property
    def tardanzas(self):
        return self.__tardanzas 
    @property
    def sueldoBas(self):
        return self.__sueldoBas 
    @property
    def descuentoTar(self):
        return self.__descuentoTar 
    @property
    def pxhe(self):
        return self.__pxhe 
    @property
    def sueldoNeto(self):
        return self.__sueldoNeto 
    @property
    def pagoxhora(self):
        return self.__pagoxhora 
    @property
    def categoria(self):
        return self.__categoria
    @property
    def newcategoria(self):
        return self.__newcategoria  
    
    
    #set
    @trabajador.setter
    def trabajador(self,trabajador):
        self.__trabajador=trabajador
    @categoria.setter
    def categoria(self,categoria):
        self.__categoria=categoria
    @he.setter
    def he(self,he):
        self.__he=he
    @tardanzas.setter
    def tardanzas(self,tardanzas):
        self.__tardanzas=tardanzas
    
    @sueldoBas.setter
    def sueldoBas(self,sueldoBas):
        self.__sueldoBas=sueldoBas
    
    @descuentoTar.setter
    def descuentoTar(self,descuentoTar):
        self.__descuentoTar=descuentoTar
        
    @pxhe.setter
    def pxhe(self,pxhe):
        self.__pxhe=pxhe
        
    @sueldoNeto.setter
    def sueldoNeto(self,sueldoNeto):
        self.__sueldoNeto=sueldoNeto
        
    @pagoxhora.setter
    def pagoxhora(self,pagoxhora):
        self.__pagoxhora=pagoxhora
        
    @categoria.setter
    def categoria(self,categoria):
        self.__categoria=categoria
        
    @newcategoria.setter
    def newcategoria(self,newcategoria):
        self.__newcategoria=newcategoria
    
    
    