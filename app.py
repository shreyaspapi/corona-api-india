from flask import Flask
import requests
from flask import jsonify
import json

data = requests.get("https://exec.clay.run/kunksed/mohfw-covid")

di = data.json()

app = Flask(__name__)


@app.route("/state_data")
def state_data():
    data_list = []
    for i, j in di["stateData"].items():
      state_data = {}
      state_data["state"] = i
      state_data["id"] = len(data_list) + 1
      for k, l in j.items():
        state_data[k] = str(l)

      data_list.append(state_data)

    return json.dumps(data_list)


@app.route("/country_data")
def imp_data():
    imp_data = di["countryData"]
    return json.dumps([imp_data])

if __name__ == '__main__':
   app.run()
