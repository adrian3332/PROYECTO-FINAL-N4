from claseMarca import Marca
from claseGrupo import Grupo
class Producto:
    def __init__(self, codigo=0, des="", pre=1, sto=1, marc= None, gru= None, est= True):
        self.id=codigo
        self.descripcion=des
        self.precio=pre
        self.stock=sto
        self.marca=marc
        self.grupo=gru 
        self.estado=est 

    def mostrarProducto(self):
        return " {} - {} - {} - {} - {} - {} - {} ".format(self.id, self.descripcion, self.precio, 
        self.stock, self.marca.descripcion, self.grupo.descripcion, self.estado)