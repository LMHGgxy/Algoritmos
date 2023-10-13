from json import load
from flask import Flask
from flask import render_template
from flask import jsonify

with open("lugares.json",encoding="utf8") as file:
    data = load(file)    


app = Flask(__name__)

@app.route("/")
def home(): return render_template("index.html",lugares=data)

@app.route("/lugares",)
def lugares(): return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000,debug=True)