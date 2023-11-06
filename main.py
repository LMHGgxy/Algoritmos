from flask import Flask, render_template, jsonify, request
from Libs.Lugares import connectionPlace
from Libs.lista import Lista

app = Flask(__name__, template_folder="templates")

Lugares = Lista()

class ConeroApp:
    def __init__(self):
        pass

    @app.route("/")
    def home():
        if request.method == 'POST':
            return jsonify({'response': 'method no allowed'}), 405
        return render_template("index.html")

    @app.route("/lugares", methods=['GET', 'POST'])
    def places():
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
                    
                return jsonify({'response': 'places added'}), 200

            except Exception as error:
                return jsonify({'response error': error}), 500

        else:
            return jsonify({'response': 'method no allowed'}), 400


if __name__ == "__main__":
    places_app = ConeroApp()
    app.run(port=5000, debug=True)
