class NodoLista:
    def __init__(self, valor):
        self.valor = valor  # El valor almacenado en el nodo
        self.siguiente = None  # El siguiente nodo en la lista, inicialmente None

class Lista:
    def __init__(self):
        self.length = 0  # La longitud de la lista, inicialmente 0
        self.head = None  # El primer nodo de la lista, inicialmente None
        self.estado = None  # Un estado para mantener el seguimiento durante las operaciones

    def append(self, value):
        # Añade un nuevo nodo con el valor dado al final de la lista
        if not self.head:
            # Si la lista está vacía, el nuevo nodo se convierte en el head
            self.head = NodoLista(value)
            self.length += 1
            self.estado = self.head
            return

        # Si la lista no está vacía, recorre hasta el último nodo
        actual = self.head
        while actual.siguiente:
            actual = actual.siguiente
        # Añade el nuevo nodo al final de la lista
        actual.siguiente = NodoLista(value)
        self.length += 1  # Incrementa la longitud de la lista

    def temporal_show(self, valor):
        # Muestra el valor actual y actualiza el estado al siguiente nodo
        self.estado = valor.siguiente
        return valor

    def show(self):
        # Muestra el valor del nodo actual y avanza el estado
        if not self.estado:
            # Si el estado es None, comienza desde el head
            self.estado = self.head
            
        # Utiliza temporal_show para obtener el valor actual y avanzar el estado
        return self.temporal_show(self.estado)

    def delete(self, value):
        # Elimina el nodo con el valor dado de la lista
        current = self.head
        previous = None
        while current:
            if current.valor == value:
                # Si el valor se encuentra, elimina el nodo de la lista
                if previous:
                    # Si hay un nodo anterior, enlaza el anterior con el siguiente del actual
                    previous.siguiente = current.siguiente
                else:
                    # Si no hay nodo anterior, el siguiente nodo se convierte en el nuevo head
                    self.head = current.siguiente
                self.length -= 1  # Decrementa la longitud de la lista
                return "deleted"
            # Continúa al siguiente nodo
            previous = current
            current = current.siguiente
        # Si el valor no se encuentra en la lista, retorna un mensaje
        return f"Value {value} not found in the list."
