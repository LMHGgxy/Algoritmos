from Libs.lista import Lista

class Nodo:
    def __init__(self, valor):
        self.valor = valor if valor is not None else None
        self.anteriores = Lista()
        self.siguientes = Lista()

class connectionPlace:
    def __init__(self):
        self.head = None
    
    def verify(self,valor):
        if not self.head:
            self.head = Nodo(valor)
    
    def add_connection(self, valor, antes=None, despues=None):
        self.verify(valor)        
        actual = self.head
        while actual:
            if valor == actual.valor:
                if antes:
                    actual.anteriores.append(antes)
                if despues:
                    actual.siguientes.append(despues)
                return "valores añadidos"
            actual = actual.siguiente.head
    
    def show(self, show_value):
        current = self.head
        if show_value in ["siguiente","despues","sig"]:
            for i in current.siguientes.show():
                yield i
                
        elif show_value in ["anterior","antes","ant"]:
            for i in current.anteriores.show():
                yield i
                
    def create_point(self,valor):
        self.verify()