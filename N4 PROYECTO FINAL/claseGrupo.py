class Grupo:
    def __init__(self, codigo, des, est= True):
        self.id=codigo
        self.descripcion=des
        self.estado=est
    
    def mostrarGrupo(self):
        return " {};{};{} ".format(self.id, self.descripcion, self.estado)
