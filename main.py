from flask import Flask, render_template, jsonify
from Libs.database_lista_enlazada_doble import *

a = Nodo(1)
b = Nodo(2)
c = Nodo(3)
d = Nodo(4)
e = Nodo(5)

app = Flask(__name__, template_folder="templates")

lista = ConnectionPlaces()

class ConeroApp:
    def __init__(self):
        pass

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/lugares")
    def places():
        return jsonify(lista.convertir_a_json())

if __name__ == "__main__":
    places_app = ConeroApp()
    app.run(port=5000, debug=True)
