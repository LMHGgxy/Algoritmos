from Libs.lista import Lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor if valor is not None else None
        self.anteriores = Lista()
        self.siguientes = Lista()


class connectionPlace:
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
        self.head = None
        self.estado = None
        self.estado_anteriores = None
        
    def verify(self,valor):
        if not self.head:
            self.head = Nodo(valor)
    
    def add_connection(self, valor, antes=None, despues=None):
        self.verify(valor)
        actual = self.head
        if valor == actual.valor:
            if antes:
                actual.anteriores.append(antes)
            if despues:
                actual.siguientes.append(despues)
        return "valores añadidos"
    
    """
    def temporal_show(self, valor, ubicacion):
            if ubicacion:
                self.estado = self.head.siguientes.show()
            else:
                self.estado_anteriores = self.head.anteriores.show()
            
            return valor
            
    def show(self, show_value):
        if show_value in ["siguiente","despues","sig"]:
            if not self.estado:
                self.estado = self.head.siguientes.show()
            valor = self.temporal_show(self.estado,True)
        elif show_value in ["anterior","antes","ant"]:
            if not self.estado_anteriores:
                self.estado_anteriores = self.head.anteriores.show()
            valor = self.temporal_show(self.estado_anteriores, False)
        
        return valor
    """