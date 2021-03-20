class Cliente:
    def __init__(self, ruc, nom, dir, tel, mail, est=True):
        self.ruc=ruc
        self.nombre=nom
        self.direccion=dir
        self.telefono=tel
        self.email=mail
        self.estado=est
    
    def mostrarCliente(self):
        return " {};{};{};{};{} ".format(self.ruc, self.direccion, 
        self.telefono, self.email)