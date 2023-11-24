import requests

data = {
    "Ancon": {
        "ir": ["Los olivos", "Chorrillos", "Miraflores"],
        "volver": ["San martin de porres", "Cercado de lima", "Lince"],
        "x": -1500,
        "y": 3500
    },
    "Cercado de lima": {
        "ir": ["Chorrillos", "San martin de porres", "Lince"],
        "volver": ["Los olivos", "Ancon", "San Isidro"],
        "x": 0,
        "y": 0
    },
    "Chorrillos": {
        "ir": ["Ancon", "Barranco"],
        "volver": ["Cercado de lima", "Miraflores"],
        "x": 2500,
        "y": -4500
    },
    "Los olivos": {
        "ir": ["San martin de porres", "Cercado de lima", "Miraflores"],
        "volver": ["Ancon", "San Isidro"],
        "x": -2500,
        "y": 4500
    },
    "San martin de porres": {
        "ir": ["Ancon", "Lince"],
        "volver": ["Los olivos", "Cercado de lima", "Surquillo"],
        "x": -3500,
        "y": 3000
    },
    "Miraflores": {
        "ir": ["San Isidro", "Barranco", "Ancon"],
        "volver": ["Surquillo", "Ancon"],
        "x": 1250,
        "y": -1250
    },
    "San Isidro": {
        "ir": ["Miraflores", "La Victoria"],
        "volver": ["Lince", "La Victoria", "Cercado de lima"],
        "x": 1750,
        "y": -6500
    },
    "Barranco": {
        "ir": ["Chorrillos", "Miraflores"],
        "volver": ["Miraflores", "Surquillo"],
        "x": 3250,
        "y": -2250
    },
    "Surquillo": {
        "ir": ["Miraflores", "San Borja"],
        "volver": ["San Borja", "San Isidro"],
        "x": 7000,
        "y": -3000
    },
    "La Victoria": {
        "ir": ["San Isidro", "Lince"],
        "volver": ["Lince", "San Borja"],
        "x": 1850,
        "y": 2000
    },
    "Lince": {
        "ir": ["La Victoria", "San Isidro"],
        "volver": ["San Isidro", "Cercado de lima"],
        "x": 1500,
        "y": 0
    },
    "San Borja": {
        "ir": ["Surquillo"],
        "volver": ["Surquillo"],
        "x": 8500,
        "y": -2250
    }
}


url = 'http://127.0.0.1:5000/lugares'

requests.post(url,json=data)

