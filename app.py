from flask import Flask
import requests
from flask import jsonify

data = requests.get("https://exec.clay.run/kunksed/mohfw-covid")

di = data.json()

app = Flask(__name__)


@app.route("/state_data")
def state_data():
    state_data = {}
    for i, j in zip(di["stateData"].items()):
        state_data["-".join(i.split())] = j
    return jsonify(state_data)


@app.route("/country_data")
def imp_data():
    imp_data = di["countryData"]
    return jsonify(imp_data)

if __name__ == '__main__':
   app.run()
