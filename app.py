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
    dd = di["data"]["summary"]
    
    data_list.insert(0, {"loc": "Total", "total": dd["total"], "confirmedCasesIndian": dd["confirmedCasesIndian"], "confirmedCasesForeign": dd["confirmedCasesForeign"], "discharged": dd["discharged"], "deaths": dd["deaths"]})

    for data in range(len(data_list)):
        a = data_list[data]["confirmedCasesIndian"]
        b = data_list[data]["confirmedCasesForeign"]
        data_list[data]["total"] = str(a + b)
        data_list[data]["id"] = data
        data_list[data]["confirmedCasesIndian"] = str(data_list[data]["confirmedCasesIndian"])
        data_list[data]["confirmedCasesForeign"] = str(data_list[data]["confirmedCasesForeign"])
        data_list[data]["discharged"] = str(data_list[data]["discharged"])
        data_list[data]["deaths"] = str(data_list[data]["deaths"])
    return json.dumps(data_list)


if __name__ == '__main__':
   app.run()
