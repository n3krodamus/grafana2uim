#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response, request
import json
import logging


## Config
dump = 'dumps/json_file.txt'
log = 'logs/grafana2uim.log'
logging.basicConfig(filename=log,
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
# Start logger
logger=logging.getLogger()
  
# DEBUG
logger.setLevel(logging.DEBUG)


## Inicio de aplicacion
app = Flask(__name__)
logger.debug("Iniciando...")


def write_to_file ( json_obj ):
    a = [ json_obj['title'],
          json_obj['ruleName'], 
          json_obj['ruleId'], 
          json_obj['state'], 
          json_obj['evalMatches'][0]['value']

        ]

    text = ','.join( map(str,a) ) 

    file = open(dump, "w") 
    file.write( text + "\n")
    file.close()
    logger.debug("Data dumped to " + dump)


## Recibe JSON
@app.route('/api/v1.0/grafana/task',methods=['POST'])
def create_task():
    #if not request.json or not 'title' in request.json:
    if not request.json:
        abort(400)
    
    write_to_file ( request.json )
    logger.debug("Request recibido")
    return jsonify({'status':'OK'}),201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}),404)


@app.route('/')
def index():
    return "Grafana to UIM - Integracion de alarmas"

if __name__ == '__main__':
    app.run(debug=True)
