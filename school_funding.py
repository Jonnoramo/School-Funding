# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'schoolfunding'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'funding status': True, 'total donationd': True, 'Price': False}

# Route to display charts

@app.route("/")

def main():

    return render_template("main.html")



# Route to display a detailed data table with data selectors

@app.route("/detail")

def detail():

    return render_template("detail.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/schoolfunding/projects")
def schoolfunding_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)