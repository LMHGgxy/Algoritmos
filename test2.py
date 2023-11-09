import networkx as nx
import matplotlib.pyplot as plt
import random

# Definimos el número de nodos y seleccionamos un número pequeño de aristas para que sea escaso
nodos = 10
max_aristas = int(nodos * (nodos - 1) / 2)  # Máximo número de aristas en un grafo completo
aristas = random.randint(nodos-1, int(max_aristas/2))  # Seleccionar un número de aristas que sea escaso

# Usar la función gnm_random_graph(n, m) que crea un grafo con n nodos y m aristas de forma aleatoria
G_escaso_random = nx.gnm_random_graph(nodos, aristas)

# Dibujar el grafo escaso aleatorio
plt.figure(figsize=(8, 6))
nx.draw(G_escaso_random, with_labels=True, node_color='lightblue', node_size=700, edge_color='grey')
plt.title("Grafo Escaso Aleatorio")
plt.show()
