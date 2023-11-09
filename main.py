from flask import Flask, render_template, jsonify, request,render_template_string
from Libs.Lugares import connectionPlace
from Libs.lista import Lista
import matplotlib
import random
matplotlib.use('Agg')

import matplotlib.pyplot as plt

import networkx as nx
import base64
import io

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
                        print(current.valor.head)
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
@app.route("/dibujar_lugares", methods=['GET'])
def draw_places():
    global lugares_to_draw
    places = lugares_to_draw

    # Crear un grafo dirigido con NetworkX
    G = nx.DiGraph()

    # Generar una paleta de colores única
    all_edges = sum([len(coords['ir']) + len(coords['volver']) for coords in places.values()])
    unique_colors = generate_unique_colors(all_edges)

    # Añadir nodos y aristas al grafo con las coordenadas especificadas
    edge_colors = []
    for place, coords in places.items():
        G.add_node(place, pos=(coords['x'], coords['y']))
        for destination in coords['ir']:
            G.add_edge(place, destination)
            edge_colors.append(unique_colors.pop())  # Asignar un color único a la arista
        for origin in coords['volver']:
            G.add_edge(origin, place)
            edge_colors.append(unique_colors.pop())  # Asignar un color único a la arista

    # Obtener la posición de cada nodo
    pos = {place: (coords['x'], coords['y']) for place, coords in places.items()}

    # Definir el tamaño de la figura y dibujar el grafo
    fig_width, fig_height = 1920 / 96, 1080 / 96
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1600)
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->', arrowsize=20, edge_color=edge_colors, node_size=2000)

    # Guardar y devolver la imagen
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=96)
    plt.close(fig)
    buf.seek(0)
    image_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return jsonify({"code_image":image_b64})

def generate_unique_colors(n):
    """Genera n colores únicos."""
    colors = []
    for i in range(n):
        colors.append('#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    random.shuffle(colors)
    return colors

    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
