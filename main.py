from flask import Flask, render_template, jsonify
from Libs.Lugares import connectionPlace
from Libs.lista import Lista

app = Flask(__name__, template_folder="templates")

Lugares = Lista()

class ConeroApp:
    def __init__(self):
        pass

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/lugares")
    def places():
        pass
        # return jsonify(lista.convertir_a_json())

if __name__ == "__main__":
    places_app = ConeroApp()
    app.run(port=5000, debug=True)
