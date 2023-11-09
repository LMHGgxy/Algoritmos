from Libs.lista import Lista  # Importa la clase Lista de un módulo o paquete llamado Libs

class Nodo:
    def __init__(self, valor):
        # Constructor de la clase Nodo, que inicializa un nodo con el valor dado.
        # Si el valor es None, se mantiene como None, de lo contrario, se asigna el valor proporcionado.
        self.valor = valor if valor is not None else None
        # Cada nodo mantiene dos listas para rastrear sus nodos anteriores y siguientes.
        self.anteriores = Lista()  # Lista de nodos anteriores.
        self.siguientes = Lista()  # Lista de nodos siguientes.

class connectionPlace:
    def __init__(self, x, y):
        # Constructor de la clase connectionPlace, que representa un lugar de conexión con coordenadas x, y.
        self.x = x  # Coordenada x
        self.y = y  # Coordenada y
        
        # El 'head' es el nodo de partida en la lista de conexiones.
        self.head = None
        # 'estado' y 'estado_anteriores' pueden ser utilizados para rastrear el estado durante la iteración o procesos.
        self.estado = None
        self.estado_anteriores = None
        
    def verify(self, valor):
        # Un método para verificar si la cabeza de la lista de conexiones está presente.
        # Si no hay cabeza, crea un nuevo Nodo con el valor dado y lo asigna como cabeza.
        if not self.head:
            self.head = Nodo(valor)
    
    def add_connection(self, valor, antes=None, despues=None):
        # Método para añadir conexiones a un nodo específico representado por 'valor'.
        # Primero verifica si la cabeza de la lista de conexiones existe.
        self.verify(valor)
        # Se asume que la cabeza siempre existe después de la verificación.
        actual = self.head
        # Si el valor actual es igual al valor del nodo, se añaden conexiones.
        if valor == actual.valor:
            if antes:
                # Si se proporciona un valor 'antes', lo añade a la lista de 'anteriores' del nodo actual.
                actual.anteriores.append(antes)
            if despues:
                # Si se proporciona un valor 'despues', lo añade a la lista de 'siguientes' del nodo actual.
                actual.siguientes.append(despues)
        return "valores añadidos"
