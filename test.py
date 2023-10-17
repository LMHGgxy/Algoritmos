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
    
for i in lugares.show():
    for o in i.show("antes"):
        print(f"antes de {i.head.valor} esta {o}")
    for o in i.show("despues"):
        print(o)