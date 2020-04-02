from flask import Flask
import requests
from flask import jsonify
import json


app = Flask(__name__)



@app.route("/data")
def state_data():
    data = requests.get("https://api.covid19india.org/data.json")
    data = data.json()["statewise"]
    d = []
    for i in data:
        d.append(dict([(str(k), str(v)) for k, v in i.items()]))

    data_list = []

    for k in range(len(d)):
        data_dict = {}
        if d[k]["confirmed"] == "0":
            break

        data_dict["confirmed"] = d[k]["confirmed"]
        data_dict["active"] = d[k]["active"]
        data_dict["deaths"] = d[k]["deaths"]
        data_dict["id"] = k
        data_dict["lastupdatedtime"] = d[k]["lastupdatedtime"]
        data_dict["recovered"] = d[k]["recovered"]
        data_dict["state"] = d[k]["state"]
        data_list.append(data_dict)
    return json.dumps(data_list)


if __name__ == '__main__':
   app.run()
