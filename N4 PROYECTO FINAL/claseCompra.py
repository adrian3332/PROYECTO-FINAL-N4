from claseMarca import Marca
from claseGrupo import Grupo
from claseProducto import Producto
from claseDetCompra import DetCompra
from claseProveedor import Proveedor
class Compra:
    def __init__(self, fact, fech, prove, sub, iva, total, det, est=True):
        self.factura=fact
        self.fecha=fech
        self.proveedor=prove
        self.subtotal=sub
        self.iva=iva
        self.total=total
        self.detalle=det
        self.estado=est
    
    def mostrarVenta(self):
        return [self.factura,
        self.fecha,
        self.proveedor,
        self.subtotal,
        self.iva,
        self.total,
        self.detalle,
        self.estado]