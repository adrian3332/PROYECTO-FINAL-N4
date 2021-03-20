from claseMarca import Marca
from claseGrupo import Grupo
from claseProducto import Producto
class DetVenta:
    def __init__(self, id, produc, prec=0, cant=0):
        self.id=id
        self.producto=produc
        self.precio=produc.precio
        self.cantidad=cant