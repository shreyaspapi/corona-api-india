from flask import Flask
import requests
from flask import jsonify
import json


app = Flask(__name__)


@app.route("/data")
def state_data():
    data = requests.get("https://api.rootnet.in/covid19-in/stats/latest")

    di = data.json()

    dd = di["data"]["summary"]
    data_list = di["data"]["regional"]

    data_list.insert(0, {"id": 0,"loc": "Total", "total": str(dd["total"]), "confirmedCasesIndian": str(dd["confirmedCasesIndian"]), "confirmedCasesForeign": str(dd["confirmedCasesForeign"]), "discharged": str(dd["discharged"]), "deaths": str(dd["deaths"])})


    for data in range(1, len(data_list)):
        a = data_list[data]["confirmedCasesIndian"]
        b = data_list[data]["confirmedCasesForeign"]
        data_list[data]["total"] = str(a + b)
        data_list[data]["id"] = data + 1
        data_list[data]["confirmedCasesIndian"] = str(data_list[data]["confirmedCasesIndian"])
        data_list[data]["confirmedCasesForeign"] = str(data_list[data]["confirmedCasesForeign"])
        data_list[data]["discharged"] = str(data_list[data]["discharged"])
        data_list[data]["deaths"] = str(data_list[data]["deaths"])
    return json.dumps(data_list)


if __name__ == '__main__':
   app.run()
