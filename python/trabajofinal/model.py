from entity import *
from util import *
        
# class Categorias:
#     def categorias(self,px):
#         if (px.categoria== 'A'):
#             px.newcategoria = 2
#             return px.newcategoria
        
#         elif (px.categoria== 'B'):
#             px.newcategoria = 3
#             return px.newcategoria
        
#         elif (px.categoria== 'C'):
#             px.newcategoria = 2
#             return px.newcategoria

class Operaciones:
    def categoriaA(self,px):
        px.sueldoBas = 3000
        px.pagoxhora = px.sueldoBas / 240
        px.descuentoTar = px.tardanzas * 0.1736
        px.pxhe = round(px.pagoxhora * 4 , 2)
        px.sueldoNeto=round(px.sueldoBas + px.pxhe - px.descuentoTar, 2)
    
    def categoriaB(self,px):
        px.sueldoBas = 2500
        px.pagoxhora = px.sueldoBas / 240
        px.descuentoTar = px.tardanzas * 0.1736
        px.pxhe = round(px.pagoxhora * 3 , 2)
        px.sueldoNeto=round(px.sueldoBas + px.pxhe - px.descuentoTar, 2)
    
    def categoriaC(self,px):
        px.sueldoBas = 2000
        px.pagoxhora = px.sueldoBas / 240
        px.descuentoTar = px.tardanzas * 0.1736
        px.pxhe = round(px.pagoxhora * 2 , 2)
        px.sueldoNeto=round(px.sueldoBas + px.pxhe - px.descuentoTar, 2)
    
    
        
        
        
        
        
        