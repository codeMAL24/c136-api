from flask import Flask,jsonify,request
from data import data
import pandas as pd

app = Flask(__name__)  

@app.route("/")
def home():
    return jsonify({
        "data": data,
        "message": "success!"
    }),200
@app.route("/star")
def planet():
    name = request.args.get("name")
    stardata = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": stardata,
        "message": "success!"
    }),200
    

if __name__ == "__main__":
    app.run(debug=True)
