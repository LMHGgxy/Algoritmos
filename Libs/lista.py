class NodoLista:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Lista:
    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = NodoLista(value)
            self.length += 1
            return
        
        actual = self.head
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoLista(value)
        self.length += 1
        
    def show(self):
        current = self.head
        while current:
            yield current.valor
            current = current.siguiente
            
    def delete(self, value):
        current = self.head
        previous = None
        while current:
            if current.valor == value:
                if previous:
                    previous.siguiente = current.siguiente
                else:
                    self.head = current.siguiente
                self.length -= 1
                return "deleted"
            previous = current
            current = current.siguiente
        return f"Value {value} not found in the list."