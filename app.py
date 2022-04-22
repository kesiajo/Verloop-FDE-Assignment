import json
from flask import Flask, Response, jsonify, request
from flask_restful import Api, Resource, reqparse
import os
import urllib.parse
import requests
from dicttoxml import dicttoxml


app = Flask(__name__)

def json_response(coordinates, address):
    return jsonify({"coordinates": coordinates, "address": address})

def xml_response(coordinates, address):
    return Response(dicttoxml({"coordinates": coordinates, "address": address}), mimetype='text/xml')


@app.route('/getAddressDetails', methods=['GET','POST'])
def getAddressDetails():
    # API_KEY= os.getenv(API_KEY)
    details = request.json
    address = details["address"]
    address_enc = urllib.parse.quote(address) 
    output_format = details["output_format"]
    API_KEY = "secret"
    URL = f"https://maps.googleapis.com/maps/api/geocode/json"
    PARAMS = {"address": address_enc, "key": API_KEY}
    response = requests.get(url = URL, params = PARAMS).json() 

    coordinates = response["results"][0]["geometry"]["location"]

    if output_format == 'json':
        return json_response(coordinates, address)
    elif output_format == 'xml':
        return xml_response(coordinates, address)


if __name__ == '__main__':
    app.run(debug = "True")

