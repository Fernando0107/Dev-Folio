from flask import Flask, render_template, jsonify, redirect
import yaml
import os
import json

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

with open('info.json') as f:
  data = json.load(f)


@app.route('/') 

def index():

    return render_template("index.html", name=data['info']["name"], phone=data['info']["phone"], mail=data['info']["mail"], profile=data['info']["profile"])


if __name__ == '__main__':

    debug=False
    if environment == "development" or environment == "local":
        debug=True

    print("Local change")

    app.run(host="0.0.0.0", debug=debug)
