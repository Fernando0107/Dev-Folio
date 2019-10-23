from flask import Flask, render_template, jsonify, redirect
import yaml
import os

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)


@app.route('/') 
def index():

    return render_template("index.html")


if __name__ == '__main__':

  app.run(host="0.0.0.0", debug=True)
