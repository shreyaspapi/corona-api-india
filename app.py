from flask import Flask, request
import requests
from flask import jsonify
import json
from datetime import datetime
from pytz import timezone
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route("/recognition", methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      data = ["yes", "no"]
      response = {"description": data[1]}
      time.sleep(5)
      return json.dumps(response)

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

        india = timezone('Asia/Kolkata')
        now = datetime.now(india)


        data_dict["confirmed"] = d[k]["confirmed"]
        data_dict["active"] = d[k]["active"]
        data_dict["deaths"] = d[k]["deaths"]
        data_dict["id"] = k
        data_dict["lastupdatedtime"] = str(now - datetime.strptime(d[k]["lastupdatedtime"], '%d/%m/%Y %H:%M:%S').replace(tzinfo=india)).split(".")[0]
        data_dict["recovered"] = d[k]["recovered"]
        data_dict["state"] = d[k]["state"]
        data_list.append(data_dict)
    return json.dumps(data_list)


if __name__ == '__main__':
   app.run()
