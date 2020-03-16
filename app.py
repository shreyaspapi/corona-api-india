from flask import Flask
import requests
from flask import jsonify
import json

data = requests.get("https://exec.clay.run/kunksed/mohfw-covid")

di = data.json()

app = Flask(__name__)


@app.route("/state_data")
def state_data():
    state_data = {}
    for i, j in di["stateData"].items():
      if "&" in i:
        continue
      try:
        state_data["_".join(i.split())] = j
      except:
        state_data[i] = j
    
    for i, j in state_data.items():
        for k, l in state_data[i].items():
          state_data[i][k] = str(l)
    da = [state_data]
    return json.dumps(da)


@app.route("/country_data")
def imp_data():
    imp_data = di["countryData"]
    return json.dumps([imp_data])

if __name__ == '__main__':
   app.run()
