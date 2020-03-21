from flask import Flask
import requests
from flask import jsonify
import json

data = requests.get("https://api.rootnet.in/covid19-in/stats/latest")

di = data.json()

app = Flask(__name__)


@app.route("/data")
def state_data():
    data_list = di["data"]["regional"]

    return json.dumps(data_list)


if __name__ == '__main__':
   app.run()
