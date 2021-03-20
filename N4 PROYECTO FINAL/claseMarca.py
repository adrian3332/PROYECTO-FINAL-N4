class Marca:
    def __init__(self, codigo, des, est):
        self.id=codigo
        self.descripcion=des
        self.estado=est
    
    def mostrarMarca(self):
        return " {};{};{} ".format(self.id, self.descripcion, self.estado)
