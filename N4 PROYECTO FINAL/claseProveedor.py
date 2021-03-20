class Proveedor:
    def __init__(self, ruc, nom, dir, tel, mail, est=True):
        self.__ruc=ruc
        self.nombre=nom
        self.direccion=dir
        self.telefono=tel
        self.email=mail
        self.estado=est

    @property
    def ruc(self):
        return self.__ruc
    
    def mostrarProveedor(self):
        return " {};{};{};{};{} ".format(self.nombre, self.ruc, self.direccion, 
        self.telefono, self.email)

class ProveedorLote(Proveedor):
    def __init__(self, ruc, nom, dir, tel, mail, ctbanco, est=True):
        super().__init__(ruc, nom, dir, tel, mail, est)
        self.cuentabanco=ctbanco

    def mostrarProveedor(self):
        mostrar = super().mostrarProveedor()
        return "{};{}".format(mostrar, self.cuentabanco)

class ProveedorMayor(Proveedor):
    def __init__(self, ruc, nom, direc, tel, mail, est, tar):
        super().__init__(ruc, nom, direc, tel, mail, est)
        self.tarjetacredito=tar
        
    def mostrarProveedor(self):
        super().mostrarProveedor()
        return " {}  ".format(self.tarjetacredito)
