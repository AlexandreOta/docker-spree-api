import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import requests
import json
import datetime

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.SpreeProd


@app.route('/')
def carga():
    
    _items = db.SpreeProd.find().sort('idExterno')
    items = [item for item in _items]
    
    return render_template('carga.html', items=items)


def carga_dados():
    
    token="e0c91507ca69781a03c62aabd83246ed75e8ed0f498a4652"
     
    url = "http://spree:3000/api/v1/products.json?token=" + token 
    
    r= requests.get(url)
    
    x= json.loads(r.text)    
    for k in x["products"]:
        item_doc = {
            'id': k['id'],
            'name': k['name'],
            'price': k['price'],
            'data' : datetime.datetime.utcnow(),
            'idExterno': request.form['idExterno']
        }
        db.SpreeProd.insert_one(item_doc)


@app.route('/new',methods=['POST'])
def new():
    carga_dados()
    return redirect(url_for('carga'))
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)