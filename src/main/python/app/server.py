from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, get_jwt
)
from datetime import datetime, timedelta, timezone

from app import app
from app.utils import init_routing_func, check_request_data
from app.obj_utils import get_objs, get_objs_with_filter, create_obj, get_obj_with_filter, get_obj, change_product
from database.tables import Gebruikers, Product, Winkelwagen, Bestellingen, BestellingItems, Maat, Kleur, Favoriet


home, get, post, put = init_routing_func('home', '/home/')

@get('/gebruikers')
def getGebruikers():
    gebruikers=get_objs(Gebruikers)
    return jsonify(gebruikers),200

@get('/product')
def getProducts():
    product=get_objs(Product)
    return jsonify(product),200

@get('/product/<string:name_id>')
def getProductsByName(name_id):
    product=get_objs_with_filter(Product, naam=name_id)
    return jsonify(product),200

@get('/product/<int:product_id>')
def getProductById(product_id):
    product=get_obj_with_filter(Product, id=product_id)
    return jsonify(product),200

@get('/product/<string:product_categorie>/<string:product_naam>')
def getProductByCategorieAndName(product_naam, product_categorie):
    product=get_objs_with_filter(Product, naam=product_naam, categorie=product_categorie)
    return jsonify(product),200

@get('/product/<string:product_categorie>/<string:product_naam>/<string:product_kleur>/<string:product_maat>')
def getFirstProduct(product_naam, product_categorie, product_kleur, product_maat):
    product=get_obj_with_filter(Product, naam=product_naam, categorie=product_categorie, kleur=product_kleur, maat=product_maat)
    return jsonify(product),200

@get('/products/<string:product_categorie>')
def getProductsByCategorie(product_categorie):
    product=get_objs_with_filter(Product, categorie = product_categorie)
    return jsonify(product),200


@get('/product/kleuren')
def getKleuren():
    kleuren=get_objs(Kleur)
    return jsonify(kleuren),200

@get('/product/maten')
def getMaten():
    maat=get_objs(Maat)
    return jsonify(maat),200

@post('/product/create')
def createProduct():
    data = request.json
    message, response_code = check_request_data(data, ["naam", "categorie", "maat", "kleur", "prijs", "voorraad", "body", "imagePath", "manufacturer", "model", "width", "height"])
    if (response_code == 200):
        newProduct = create_obj(Product, data)
        #optioneel om ook weer het product te zien die aangemaakt wordt
        message = jsonify(newProduct.to_dict())
    return message, response_code

@put('/product/update')
def updateProduct():
    data = request.json
    message, response_code = check_request_data(data,
                                                ["id", "naam", "categorie", "maat", "kleur", "prijs", "voorraad", "body",
                                                 "imagePath", "manufacturer", "model", "width", "height"])
    if (response_code == 200):
        newProduct = change_product(Product, data)
        # optioneel om ook weer het product te zien die aangemaakt wordt
        message = jsonify(newProduct.to_dict())
    return message, response_code

