from claseMarca import Marca
from claseGrupo import Grupo
from claseProducto import Producto
from claseDetVenta import DetVenta
from claseCliente import Cliente
class Venta:
    def __init__(self, fact, fech, clien, sub, iva, total, det, est=True):
        self.factura=fact
        self.fecha=fech
        self.cliente=clien
        self.subtotal=sub
        self.iva=iva
        self.total=total
        self.detalle=det
        self.estado=est
    
    def mostrarVenta(self):
        return [self.factura,
        self.fecha,
        self.cliente,
        self.subtotal,
        self.iva,
        self.total,
        self.detalle,
        self.estado]