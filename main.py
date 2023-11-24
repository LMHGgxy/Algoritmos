from flask import Flask, render_template, jsonify, request,render_template_string
from Libs.Lugares import connectionPlace
from Libs.lista import Lista
import matplotlib
import random
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import networkx as nx

matplotlib.use('Agg')

app = Flask(__name__, template_folder="templates")

Lugares = Lista()
lugares_to_draw = None

@app.route("/")
def home():
        if request.method == 'POST':
            return jsonify({'response': 'method no allowed'}), 405
        return render_template("index.html")
    
@app.route("/lugares", methods=['GET', 'POST'])
def places():
        global lugares_to_draw
        if request.method == 'GET':
            try:
                places = {}
                current = Lugares.show()
                cantidad = 0
                try:
                    while True:
                        places[current.valor.head.valor] = {"ir":[],"volver":[],'x':current.valor.x,'y':current.valor.y}
                        cantidad_ir_volver = 0
                        try:
                            current_ir = current.valor.head.siguientes.show()
                            while True:
                                places[current.valor.head.valor]["ir"].append(current_ir.valor)
                                if cantidad_ir_volver == current.valor.head.siguientes.length - 1:
                                    cantidad_ir_volver = 0
                                    break
                                current_ir = current.valor.head.siguientes.show()
                                cantidad_ir_volver+=1
                                
                        except:
                            pass
                        try:
                            current_volver = current.valor.head.anteriores.show()
                            while True:
                                places[current.valor.head.valor]["volver"].append(current_volver.valor)
                                if cantidad_ir_volver == current.valor.head.anteriores.length - 1:
                                    cantidad_ir_volver = 0
                                    break
                                current_volver = current.valor.head.anteriores.show()
                                cantidad_ir_volver+=1
                        except:
                            pass
                        current = Lugares.show()
                        if cantidad == Lugares.length:
                            break
                        cantidad +=1
                except:
                    pass
                lugares_to_draw = places
                return jsonify(places),200
            except Exception as error:
                return jsonify({'response error': error}), 500
            
        elif request.method == 'POST':
            try:
                places = request.json
                for lugar in places:
                    valor = connectionPlace(x = places[lugar]["x"], y = places[lugar]["y"])
                    if [len(places[lugar]['ir']),len(places[lugar]['volver'])] == [0,0]:
                        return jsonify({'response error': "necesitas minimo 1 de ida o vuelta"}), 400
                    
                    for i in places[lugar]['ir']:
                        valor.add_connection(lugar, despues=i)
                    for i in places[lugar]['volver']:
                        valor.add_connection(lugar, antes=i)
                    Lugares.append(valor)
                lugares_to_draw = places
                return jsonify({'response': 'places added'}), 200
            
            except Exception as error:
                return jsonify({'response error': error}), 500
            
        else:
            return jsonify({'response': 'method no allowed'}), 400


def create_places_graph(argumento_draw):
    # Crear un grafo dirigido con NetworkX
    G = nx.DiGraph()

    # Añadir nodos y aristas al grafo con las coordenadas especificadas
    connections = []  # Lista para almacenar información sobre conexiones
    for place, coords in argumento_draw.items():
        G.add_node(place, pos=(coords['x'], coords['y']))
        for destination in coords['ir']:
            G.add_edge(place, destination)
            connections.append({"from": place, "to": destination, "type": "ir"})
        for origin in coords['volver']:
            G.add_edge(origin, place)
            connections.append({"from": origin, "to": place, "type": "volver"})

    # Obtener la posición de cada nodo
    pos = nx.get_node_attributes(G, 'pos')

    # Crear un gráfico interactivo con Plotly
    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        x_list = list(edge_trace['x'])
        x_list += [x0, x1, None]
        edge_trace['x'] = tuple(x_list)

        y_list = list(edge_trace['y'])
        y_list += [y0, y1, None]
        edge_trace['y'] = tuple(y_list)

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            )
        )
    )

    for node in G.nodes():
        x, y = pos[node]
        x_list = list(node_trace['x'])
        y_list = list(node_trace['y'])
        text_list = list(node_trace['text'])

        x_list += [x]
        y_list += [y]
        text_list += [node]

        node_trace['x'] = tuple(x_list)
        node_trace['y'] = tuple(y_list)
        node_trace['text'] = tuple(text_list)

    layout = dict(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=0),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )

    fig = dict(data=[edge_trace.to_plotly_json(), node_trace.to_plotly_json()], layout=layout)
    fig['connections'] = connections

    return fig


@app.route("/dibujar_lugares", methods=['GET'])
def draw_places():
    global lugares_to_draw
    places = lugares_to_draw

    return create_places_graph(places)


def generate_unique_colors(n):
    """Genera n colores únicos."""
    colors = []
    for i in range(n):
        colors.append('#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    random.shuffle(colors)
    return colors

# a*

def A_STAR(grafo, inicio, destino):
    nodos_pendientes = [(0, inicio)]
    distancia_total = {inicio: 0}
    nodo_anterior = {inicio: None}

    while nodos_pendientes:
        nodo_actual = min(nodos_pendientes, key=lambda x: x[0])[1]
        nodos_pendientes.remove((distancia_total[nodo_actual], nodo_actual))

        if nodo_actual == destino:
            camino = []
            while nodo_actual is not None:
                camino.insert(0, nodo_actual)
                nodo_actual = nodo_anterior[nodo_actual]
            return camino

        for vecino in grafo[nodo_actual]["ir"] + grafo[nodo_actual]["volver"]:
            nueva_distancia = distancia_total[nodo_actual] + 1

            if vecino not in distancia_total or nueva_distancia < distancia_total[vecino]:
                distancia_total[vecino] = nueva_distancia
                nodo_anterior[vecino] = nodo_actual
                nodos_pendientes.append((nueva_distancia, vecino))

    return None


@app.route("/buscar", methods=['POST'])
def buscar():
    global lugares_to_draw
    data = request.json

    if 'inicio' in data and 'final' in data:
        start = data["inicio"]
        end = data["final"]

        if start in lugares_to_draw:
            if end in lugares_to_draw[start]['ir'] + lugares_to_draw[start]['volver']:
                return jsonify({'response': 'puede ir directamente a su destino'})
            else:
                # Buscar un camino utilizando el algoritmo A* (previamente definido)
                camino = A_STAR(lugares_to_draw, start, end)
                print(camino)
                if camino:
                    resultado = {clave: lugares_to_draw[clave] for clave in camino if clave in lugares_to_draw}
                    for i in resultado:
                        
                        resultado[i]['ir'] = [ x for x in resultado[i]['ir'] if x in camino ]
                        resultado[i]['volver'] = [ x for x in resultado[i]['volver'] if x in camino ]

                    return {'response': f'Camino encontrado', 'grafo': create_places_graph(resultado)}
                else:
                    return jsonify({'response': 'No hay camino disponible'})
        else:
            return jsonify({'response': 'Lugar de inicio no encontrado'})

    else:
        return jsonify({'response': 'Envíe datos de inicio y final'})
    
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
