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
    
    for data in range(len(data_list)):
        a = data_list[data]["confirmedCasesIndian"]
        b = data_list[data]["confirmedCasesForeign"]
        data_list[data]["total"] = a + b 
        data_list[data]["id"] = data



    return json.dumps(data_list)


if __name__ == '__main__':
   app.run()
