from Libs.Lugares import connectionPlace
from Libs.lista import Lista

places = {
    "Peru":{
        "ir": ["ecuador","chile"],
        "volver":[]
    },
    "Chile":{
        "ir":["rusia","japon"],
        "volver":["Peru"]
    }
}

lugares = Lista()

for lugar in places:
    valor = connectionPlace()
    for i in places[lugar]['ir']:
        valor.add_connection(lugar,despues=i)
    for i in places[lugar]["volver"]:
        valor.add_connection(lugar,antes=i)
    lugares.append(valor)

print(places)