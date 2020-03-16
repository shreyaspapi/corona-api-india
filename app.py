from flask import Flask
import requests
from flask import jsonify

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
    return "[{}]".format(state_data)


@app.route("/country_data")
def imp_data():
    imp_data = di["countryData"]
    return "[{}]".format(imp_data)

if __name__ == '__main__':
   app.run()
