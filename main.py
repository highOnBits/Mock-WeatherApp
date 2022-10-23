from flask import Flask, request
from flask import jsonify
import requests
import json


class res:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __init__(self, temp):
        self.main = temp


class res2:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __init__(self, temp):
        self.temp = temp

app = Flask(__name__)


@app.route("/data/2.5/weather", methods=["GET"])
def index():
    args = request.args
    city = args.get("q")
    if city == "unkown":
        return "City Not found", 400

    if not city:
        return "Internal Server Error", 500

    tempRes2 = res2(38.9)
    tempResponse = res(tempRes2)
    return tempResponse.toJSON()


if __name__ == "__main__":
    app.run()
